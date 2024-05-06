def decode(message_file):
    # Step 1: Read the file and create a mapping of numbers to words
    num_to_word = {}
    with open(message_file, 'r') as file:
        for line in file:
            parts = line.split(maxsplit=1)
            num = int(parts[0])
            word = parts[1].strip()
            num_to_word[num] = word

    # Step 2: Determine the number of lines in the pyramid
    max_num = max(num_to_word.keys())
    n = 1
    total_numbers = 0
    while total_numbers < max_num:
        total_numbers += n
        n += 1
    n -= 1  # Adjust to find the correct number of lines
    
    # Step 3: Collect words that are at the end of each pyramid line
    message_words = []
    current_num = 0
    for i in range(1, n + 1):
        current_num += i
        if current_num in num_to_word:
            message_words.append(num_to_word[current_num])

    # Step 4: Concatenate the words to form the decoded message
    decoded_message = ' '.join(message_words)
    
    return decoded_message



message_file_path = r"C:\pyhton progs\coding_qual_input.txt"
decoded_message = decode(message_file_path)
print(decoded_message)  # Output: I love computers