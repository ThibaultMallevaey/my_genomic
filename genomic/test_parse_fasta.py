import genomic.tools.tool
import os

def test_parse_fasta():
    assert genomic.tools.tool.parse_fasta("example/example.fa") == {'': 'example/example.fa'}

