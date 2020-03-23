#
# mkSelectLists.py
#
# Read config files and generate parts of the web interface:
#    - option list of the annotation sets
#    - option list of the ontologies
#

import sys
import ConfigParser
import Vlad

cp = ConfigParser.ConfigParser()
cp.read(sys.argv[1])
v = Vlad.Vlad()
oconfigs = v.getOntologyConfig(cp)
aconfigs = v.getAnnotationSetConfig(cp, oconfigs)

print mkOntologyOptionList(oconfigs)
print mkAnnotationSetOptionList(aconfigs)
