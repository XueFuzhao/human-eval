"""

python utils/convert.py
evaluate_functional_correctness data\test_samples.jsonl --problem_file=data\human-eval-v2-20210705.jsonl
"""

import json

# Read the input JSONL file
input_file_path = 'data/test.jsonl'
output_file_path = 'data/test_samples.jsonl'

output_data = []

with open(input_file_path, 'r') as input_file:
    for line in input_file:
        example = json.loads(line.strip())
        completion = example['output'].replace('<extra_id_0>', '')

        output_example = {
            'task_id': example['input']["task_id"],
            'completion': completion.strip()
        }
        print(output_example['completion'])

        output_data.append(output_example)

# Write the output JSONL file
with open(output_file_path, 'w') as output_file:
    for example in output_data:
        output_file.write(json.dumps(example) + '\n')
