import setuptools
setuptools.setup(
    name = "my-genomic",
    description="un module pour lire les fichiers fasta",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["my-genomic = genomic.genomic:run"]},
)


