import eventlet


def handle(fd):
    print("client connected")
    while True:
        # pass through every non-eof line
        x = fd.readline()
        if not x:
            break
        fd.write(x)
        fd.flush()
        print("echoed", x, end=" ")
    print("client disconnected")


if __name__ == "__main__":
    server = eventlet.listen(("0.0.0.0", 6000))
    pool = eventlet.GreenPool(10000)
    while True:
        try:
            new_sock, address = server.accept()
            print("accepted", address)
            pool.spawn_n(handle, new_sock.makefile("rw"))
        except (SystemExit, KeyboardInterrupt):
            break
