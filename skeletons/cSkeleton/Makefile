# -*- Makefile -*-

flags = -Wall -O2 -g -Wno-pointer-sign

bookgen_srcs = hfbookgen.c bookgen.c book.c util.c
bookgen_hdrs = hfbookgen.h book.h hfmsgs.h util.h

decode_srcs = hfdecode.c decode.c util.c
decode_hdrs = hfdecode.h hfmsgs.h util.h itch18.h

dump_srcs = hfdump.c dump.c util.c
dump_hdrs = hfdump.h hfmsgs.h util.h

reverse_srcs = hfreverse.c reverse.c util.c
reverse_hdrs = hfreverse.h hfmsgs.h util.h

select_srcs = hfselect.c select.c util.c
select_hdrs = hfselect.h hfmsgs.h util.h

programs = hfbookgen hfdecode hfdump hfreverse hfselect

######################################################################

default: $(programs)

hfbookgen: Makefile $(bookgen_srcs) $(bookgen_hdrs)
	gcc $(flags) -o $@ $(bookgen_srcs)

hfdecode: Makefile $(decode_srcs) $(decode_hdrs)
	gcc $(flags) -o $@ $(decode_srcs)

hfdump: Makefile  $(dump_srcs) $(dump_hdrs)
	gcc $(flags) -o $@ $(dump_srcs)

hfreverse: Makefile  $(reverse_srcs) $(reverse_hdrs)
	gcc $(flags) -o $@ $(reverse_srcs)

hfselect: Makefile  $(select_srcs) $(select_hdrs)
	gcc $(flags) -o $@ $(select_srcs)

clean:
	rm -f $(programs) *~
