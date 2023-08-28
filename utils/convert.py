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

        completion = completion.replace("\t", "    ")
        completion = completion.lstrip("\n")
        completion = completion.split("\n\n")[0]
        completion = completion.replace("\r", "")
        if "```python" in completion:
            def_line = completion.index("```python")
            completion = completion[def_line:].strip()
            completion = completion.replace("```python", "")
            # print(completion)
            try:
                next_line = completion.index("```")
                completion = completion[:next_line].strip()
            except:
                print(completion)
                print("================\n")
            # print(completion)
        if '__name__ == "__main__"' in completion:
            next_line = completion.index('if __name__ == "__main__":')
            completion = completion[:next_line].strip()
            # print(completion)

        if "# Example usage" in completion:
            # print(completion)
            next_line = completion.index("# Example usage")
            completion = completion[:next_line].strip()


        output_example = {
            'task_id': example['input']["task_id"],
            'completion': completion
        }
        print(output_example['completion'])

        output_data.append(output_example)

# Write the output JSONL file
with open(output_file_path, 'w') as output_file:
    for example in output_data:
        output_file.write(json.dumps(example) + '\n')
