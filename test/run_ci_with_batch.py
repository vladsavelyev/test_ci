# import hailtop.batch as hb
# import sys

# backend = hb.ServiceBackend('vladislavsavelyev-trial', 'playground-au')

# b = hb.Batch(backend=backend, name='test_ci')

# j = b.new_job(name='hello')
# j.image(sys.argv[1])
# j.command('''
# DIR="test"
# OUT_BUCKET="${DIR}/test_run"
# test_ci "${DIR}/toy.g.vcf.bgz" "$OUT_BUCKET/toy.mt"
# ls $OUT_BUCKET
# test -e $OUT_BUCKET/toy.mt/_SUCCESS
# ''')

import os
cmd = """curl -d '{"billing_project": "vladislavsavelyev-trial", "n_jobs": 1, "token": "ZuGgn34_ifD6vS2MOLhlWZ6Xg5V2Xtg34bLXg1qusTA", "attributes": {"name": "test_ci"}}' -H "Content-Type: application/json" -H "Authorization: ***" -X POST https://batch.hail.populationgenomics.org.au/api/v1alpha/batches/create"""
print(cmd)
os.system(cmd)
print()

# b.run(open=True)
