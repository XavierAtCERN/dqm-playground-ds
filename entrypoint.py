"""
Entrypoint script which runs eternally, waiting for 
socket commands to start kedro pipelines
"""
import asyncio
import logging

logger = logging.getLogger(__name__)

CMD_TO_ACTION_MAP_SUBPROCESS = {"RUN_PIPELINE": "kedro run"}


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f"[{cmd!r} exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")


# Based on https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-server-using-streams
async def handle_echo(reader, writer):
    command = None
    while command != "QUIT":
        data = await reader.read(100)
        command = data.decode().strip()
        addr = writer.get_extra_info("peername")

        print(f"Received {command!r} from {addr!r}")

        # Check if requested action exists
        if command in CMD_TO_ACTION_MAP_SUBPROCESS:
            writer.write(
                f"Requested action {command!r} : {CMD_TO_ACTION_MAP_SUBPROCESS[command]}\n".encode()
            )
            await writer.drain()
            await run(CMD_TO_ACTION_MAP_SUBPROCESS[command])
        else:
            writer.write(f"Requested action {command!r} not found\n".encode())
            await writer.drain()

    print("Closed the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, "127.0.0.1", 8888)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
