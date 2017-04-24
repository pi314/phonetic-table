OUTPUT=output
PATCHES=patches

database.vim: output patch build_database.py
	python build_database.py > ${OUTPUT}/database.vim

patch: output mapping.txt
	sh -c 'if [ -d ${PATCHES} ]; then for f in $$(ls -1 ${PATCHES}); do cp ${PATCHES}/$${f} ${OUTPUT}; pushd ${OUTPUT}; patch <$${f}; rm $${f}; popd; done; fi'

mapping.txt: output mcbopomofo_mapping.txt
	cat ${OUTPUT}/mcbopomofo_mapping.txt > ${OUTPUT}/mapping.txt

mcbopomofo_mapping.txt: output McBopomofo/BPMFBase.txt McBopomofo/BPMFMappings.txt build_mcbopomofo_mapping.py
	python build_mcbopomofo_mapping.py > ${OUTPUT}/mcbopomofo_mapping.txt

code_comb.vim: output symbol-combinations.txt code_comb.py
	python code_comb.py > ${OUTPUT}/code_comb.vim

output:
	if [ ! -d ${OUTPUT} ]; then mkdir ${OUTPUT}; fi

clean:
	rm -rf ${OUTPUT}
