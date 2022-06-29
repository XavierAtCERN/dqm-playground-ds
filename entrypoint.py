"""
Entrypoint script which runs eternally, waiting for 
socket commands to start kedro pipelines
"""
import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    style="{",
    format="{levelname} - {asctime} - {module} - {message}",
)
logger = logging.getLogger(__name__)


HOST = "0.0.0.0"
PORT = 8888

# Map command to subprocess to run
# TODO: check how to run kedro programmatically instead of
# running it as a subprocess
CMD_TO_ACTION_MAP_SUBPROCESS = {"RUN_PIPELINE": "kedro run"}


async def run(cmd):
    """
    Coroutine which runs a subprocess on the system

    https://docs.python.org/3/library/asyncio-subprocess.html
    """
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f"[{cmd!r} exited with {proc.returncode}]")
    if stdout:
        logger.info(f"[stdout]\n{stdout.decode()}")
    if stderr:
        logger.error(f"[stderr]\n{stderr.decode()}")


async def handle_client(reader, writer):
    """
    Coroutine which handles I/O for clients connected to socket server

    https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-server-using-streams
    """
    command = None

    # TODO: check message received
    while command != "QUIT":
        data = await reader.read(100)
        command = data.decode().strip()
        addr = writer.get_extra_info("peername")

        logger.info(f"Received {command!r} from {addr!r}")

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

    logger.info("Closed the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    logger.info(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
