import hailtop.batch as hb
import sys

# backend = hb.ServiceBackend('cpg-ci', 'cpg-ci')
backend = hb.ServiceBackend('vladislavsavelyev-trial', 'playground-au')

b = hb.Batch(backend=backend, name='test_ci')

j = b.new_job(name='hello')
j.image(sys.argv[1])
j.command('''
gcloud -q auth activate-service-account --key-file=/gsa-key/key.json
python install-gcs-connector -k /gsa-key/key.json

BUCKET=gs://playground-au/test_ci
vcf2mt "${BUCKET}/toy.g.vcf.bgz" "${BUCKET}/toy.mt"
gsutil ls "${BUCKET}/toy.mt/_SUCCESS"
''')

b.run(open=True)

