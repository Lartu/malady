# +-----------------+
# | Malady Makefile |
# +-----------------+

# Other stuff
SOURCE = malady.py
CSOURCE = malady.c
OUT = malady

all: $(CSOURCE)
	$(CC) $(CSOURCE) `/usr/bin/python3-config --cflags --ldflags` -v -fPIC -o $(OUT)

$(CSOURCE): $(SOURCE)
	cython -3 --embed $(SOURCE)

clean:
	rm -f $(CSOURCE) $(OUT)

install: $(OUT)
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -m 775 $(OUT) $(DESTDIR)$(PREFIX)/bin/

uninstall:
	rm $(DESTDIR)$(PREFIX)/bin/$(OUT)
