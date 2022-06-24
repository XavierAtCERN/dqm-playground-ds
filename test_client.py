"""
Test client for the socket server responsible
for launching kedro pipelines
"""

import asyncio
import logging

# TODO: DRY
CMD_TO_ACTION_MAP_SUBPROCESS = {"RUN_PIPELINE": "kedro run"}

logging.basicConfig(
    level=logging.DEBUG,
    style="{",
    format="{levelname} - {asctime} - {module} - {message}",
)
logger = logging.getLogger(__name__)
ADDRESS = "127.0.0.1"
PORT = 8888


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(ADDRESS, PORT)

    logger.info(f"Send: {message!r}")
    writer.write(message.encode())

    data = await reader.read(100)
    logger.debug(f"Received: {data.decode()!r}")

    logger.info("Close the connection")
    writer.close()


if __name__ == "__main__":
    command = None
    while command != "quit":
        command = input("Input command to execute: ")
        if command in CMD_TO_ACTION_MAP_SUBPROCESS:
            asyncio.run(tcp_echo_client(command))
