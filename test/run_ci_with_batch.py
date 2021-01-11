import hailtop.batch as hb
import sys

backend = hb.ServiceBackend('vladislavsavelyev-trial', 'playground-au')

b = hb.Batch(backend=backend, name='test_ci')

j = b.new_job(name='hello')
j.image(sys.argv[1])
j.command('''
DIR="test"
OUT_BUCKET="${DIR}/test_run"
vcf2mt "${DIR}/toy.g.vcf.bgz" "$OUT_BUCKET/toy.mt"
ls $OUT_BUCKET
test -e $OUT_BUCKET/toy.mt/_SUCCESS
''')

b.run(open=True)
