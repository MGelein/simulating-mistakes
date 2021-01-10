venetus_a_lines = []
venetus_a_identifier = 'urn:cts:greekLit:tlg0012.tlg001.msA:'
identifier_length = len(venetus_a_identifier)
with open('hmt-2020i-texts.cex', 'r', encoding='utf8') as f:
    for line in f.readlines():
        if line[:identifier_length] == venetus_a_identifier:
            print(line)