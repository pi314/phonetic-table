OUTPUT=output

all:
	true
	make code_comb.vim
	make mapping.txt

clean:
	rm -rf ${OUTPUT}

code_comb.vim: symbol-combinations.txt code_comb.py
	if [ ! -d ${OUTPUT} ]; then mkdir ${OUTPUT}; fi
	python code_comb.py > ${OUTPUT}/code_comb.vim

mcbopomofo_mapping.txt: McBopomofo/BPMFBase.txt McBopomofo/BPMFMappings.txt build_mcbopomofo_mapping.py
	python build_mcbopomofo_mapping.py > ${OUTPUT}/mcbopomofo_mapping.txt

mapping.txt: mcbopomofo_mapping.txt
	if [ ! -d ${OUTPUT} ]; then mkdir ${OUTPUT}; fi
	rm -f ${OUTPUT}/mapping.txt
	cat ${OUTPUT}/mcbopomofo_mapping.txt > ${OUTPUT}/mapping.txt

database.vim: mapping.txt build_databse.py
	if [ ! -d ${OUTPUT} ]; then mkdir ${OUTPUT}; fi
	python build_databse.py
