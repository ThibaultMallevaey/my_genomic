import os
import genomic.tools.tool as tool

def test_read_file():
    assert tool.read_file("example/example.fa") == ['>seq1\n', 'ATG\n', '>seq2\n', 'GTA\n']
