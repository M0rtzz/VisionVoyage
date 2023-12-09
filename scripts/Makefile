CC = g++
CFLAGS = -std=c++17
LIBS = `pkg-config --cflags --libs opencv4`

all: gray2color 

gray2color: gray2color.cc
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)


VisionVoyageServer: VisionVoyageServer.c
	gcc $< -o $@

.PHONY: clean
clean:
	rm -f gray2color VisionVoyageServer

