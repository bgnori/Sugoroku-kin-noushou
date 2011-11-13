
#sugoroku_kinnosho.txt: header.txt page*.txt
#	cat

.SUFFIXES: 
.SUFFIXES: .html .txt .ok
.PHONY: clean all test

STEM=\
	header\
	page672\
	page673\
	page674\
	page675\
	page676\
	page677\
	page678\
	page679\
	page680\
	page681\
	page682\
	page683\
	page684\
	page685\
	page686\
	page687\
	page688\
	page689

TARGET=sugoroku_kinnnoushou.txt
#
#	cat

all: $(TARGET) 

test: $(STEM:=.ok) $(STEM.=html)

clean:
	rm -f $(STEM:=.html) $(STEM:=.ok) $(TARGET)

.SECONDARY: $(STEM:=.html)

%.txt:

%.html: %.txt 
	python validate.py < $< > $@

%.ok: %.html
	python check.py $< -o $@

$(TARGET): $(STEM:=.ok)
	cat $(STEM:=.ok) > $@

