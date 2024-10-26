import time
import webbrowser
import sys
import random


def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\rLoading " + animation[i % len(animation)])
        sys.stdout.flush()

def loading_bar(iterable, total=None, prefix='Progress:', suffix='Complete', length=50, fill='█'):
    total = total or len(iterable)
    start_time = time.time()

    def print_progress_bar(iteration):
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)

        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
        sys.stdout.flush()

    for i, item in enumerate(iterable, 1):
        yield item
        print_progress_bar(i)

    sys.stdout.write('\n')
    elapsed_time = time.time() - start_time
    print(f'Total time: {elapsed_time:.2f} seconds')



def matrix_effect(rows=30, columns=80):
    chars = ['0', '1']
    for _ in range(rows):
        line = ''.join(random.choice(chars) for _ in range(columns))
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(0.1)


print("Initializing hacking sequence...")
matrix_effect()

print("\nDecrypting firewalls...")
for _ in loading_bar(range(10), prefix='Loading:', suffix='', length=10, fill='█'):
    time.sleep(0.2)

print("\nBypassing security protocols...")
for _ in loading_bar(range(15), prefix='Loading:', suffix='', length=15, fill='█'):
    time.sleep(0.2)

print("\nAccessing the mainframe...")
loading_animation()
time.sleep(2)

print("\nCompiling encrypted data...")
loading_animation()
time.sleep(2)

print("\nLoading hacking tool...")
for _ in loading_bar(range(20), prefix='Loading:', suffix='', length=20, fill='█'):
    time.sleep(2)



# Open Google in the default web browser
webbrowser.open("https://www.google.com")

print("Hacking complete! Remember to use your powers wisely.")
