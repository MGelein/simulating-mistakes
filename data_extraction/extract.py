venetus_a = {}
venetus_a_identifier = 'urn:cts:greekLit:tlg0012.tlg001.msA:'
identifier_length = len(venetus_a_identifier)
with open('hmt-2020i-texts.cex', 'r', encoding='utf8') as f:
    for line in f.readlines():
        if line[:identifier_length] == venetus_a_identifier:
            parts = line.split('#')
            if len(parts) == 2:
                urn, greek = line.split("#")
                urn = urn.replace(venetus_a_identifier, '')
                book, lineno = urn.split('.')
                book_name = 'book_' + book

                if book_name not in venetus_a: venetus_a[book_name] = []
                venetus_a[book_name].append(greek)
            else:
                pass
                # Should only trigger on the header

for book, lines in venetus_a.items():
    with open('venA_' + book + '.txt', 'w', encoding='utf8') as f:
        for line in lines: f.write(line)