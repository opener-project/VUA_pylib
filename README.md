#VUA_pylib#

Library in python with includes several functionalities for dealing with NAF/KAF files

The library is a python package and it is divided into several subpackages

##VUA_pylib.feature_extractors##

Contains functions to extract information from a NAF/KAF file

###VUA_pylib.feature_extractors.constituency###


####class Cconstituency_extractor####

Extract information from the constituency layer in a NAF file

Functions
+ get_deepest_phrase_for_termid(termid): gets the deepest phrase type for a term identifier AND the list of termids in that same chunk
+ get_least_common_subsumer(termid1, termid2): gets the least common subsumer of both ids in the constituency tree
+ get_path_from_to(term1,term2): path in the constituency tree from term1 to term2
+ get_path_for_termid(termid): constituency type path from termid to sentence root+
+ get_chunks(chunk_type): gets all the chunks for taht type
+ get_all_chunks_for_term(termid): gets all pairs (chunk_type, list_ids) of all chunks where the termid is contained

Usage:

````
from NafParserPy import NafParser
from VUA_pylib.feature_extractor.constituency import Cconstituency_extractor

file='naf_examples/10007YRK-H1B1-2SFM-K2HY.txt_8795bbbd2f30103f0ef2f098a183c457.naf'
naf_obj = NafParser(file)

extractor = Cconstituency_extractor(naf_obj)
print extractor.get_deepest_phrase_for_termid('t363')
print extractor.get_path_from_to('t363','t365')
for ch in extractor.get_chunks('NP'):
    print ch
    print [naf_obj.get_term(i).get_lemma() for i in ch]

for type_chunk, list_ids in extractor.get_all_chunks_for_term('t713'):
    print type_chunk, list_ids
````

###VUA_pylib.feature_extractors.dependency###

####class Cdependency_extractor###

Extract information from the dependency layer in a NAF file

Functions
+ get_shortest_path(term1,term2) --> gets the shortest dependency path from term1 to term2
+ get_shortest_path_spans(span1,span2) --> gets the shortest dependency path between 2 span of term ids
+ get_path_to_root(termid) --> gets the shortest dependency path from the termid to the sentence root
+ get_shortest_path_to_root_span(span) --> gets the shortest dependency path from the span of termids to the sentence root

````
from NafParserPy import NafParser
from VUA_pylib.feature_extractor.dependency import Cdependency_extractor

file='naf_examples/10007YRK-H1B1-2SFM-K2HY.txt_8795bbbd2f30103f0ef2f098a183c457.naf'
naf_obj = NafParser(file)


extractor = Cdependency_extractor(naf_obj)

p = extractor.get_shortest_path('t446','t453')
p2 = extractor.get_shortest_path_spans(['t444','t445','t446'], ['t451','t452','t454'])
p3 = extractor.get_path_to_root('t460')
p4 = extractor.get_shortest_path_to_root_span(['t444','t445','t446'])
````


Contact
------
* Ruben Izquierdo
* Vrije University of Amsterdam
* ruben.izquierdobevia@vu.nl


