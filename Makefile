all: output/phonetic_table_ipa.vim values.py values.vim brackets1.py brackets2.py


brackets1.py : output/phonetic_table.py
	cat $^ | grep '{}'  | sort > $@


brackets2.py : output/phonetic_table_ipa.vim
	cat $^ | grep '{}' | sed 's/let s:table/table/' | sort > $@


values.py: output/phonetic_table.py
	cat $^ | sed 's/^\(.*\) = \(.*\)$$/\2 = \1/' | sort > $@


values.vim: output/phonetic_table_ipa.vim
	cat $^ | sed 's/^\(.*\) = \(.*\)$$/\2 = \1/' | sort > $@


output/phonetic_table_ipa.vim: phonetic_table.py change-key.py zhuyin-pinyin-ipa-table | output
	python change-key.py > output/phonetic_table_ipa.vim


output:
	mkdir $@

phonetic_table.py: phonetic_table.vim | output
	cat phonetic_table.vim | sed -n '/^let s:table/{s/let s:table/table/; p;}' > output/$@
	ln -sf output/phonetic_table.py


clean:
	rm -r output
