
BIN = lab9a lab9b lab9c lab9d


all: $(BIN)

lab9a: lab9a.c
	cc -o lab9a lab9a.c

lab9b: lab9b.c
	cc -g -o lab9b lab9b.c

lab9c: lab9c.c
	cc -static -o lab9c lab9c.c

lab9d: lab9a.c
	cc -o lab9d lab9a.c
	strip lab9d

clean:
	-rm -f $(BIN)

