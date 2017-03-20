cat revised.patch revised.txt | grep -v '(' | sort | uniq > combine.txt
