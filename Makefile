all: phonetic_table.py change-key.py
	python change-key.py


output:
	mkdir $@

phonetic_table.py: phonetic_table.vim | output
	cat phonetic_table.vim | sed -n '/^let s:table/{s/let s:table/table/; p;}' > output/$@
	ln -sf output/phonetic_table.py


clean:
	rm -r output
