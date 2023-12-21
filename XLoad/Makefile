include Rules.make

APP = xload

all: $(APP)

$(APP): xload.cpp	
	clang++ XLoad.cpp -o $(APP) $(CFLAGS)
	
clean:
	-rm -f *.o ; rm $(APP)
