from collections import Counter
polymer, insert_data = open('./input.txt').read().split('\n\n')

insert = [l.split(' -> ') for l in insert_data.split('\n') if l]
insert_dict = {i: Counter([i[0]+m, m+i[1]]) for i, m in insert}

def main(steps):
    pol_counts = Counter([c + polymer[i+1] for i, c in enumerate(polymer[:-1])])

    for s in range(steps):
        n_pol_counts = Counter()
        for pair, count in pol_counts.items():
            n_pol_counts += {k: count*v for k,v in insert_dict[pair].items()}
        pol_counts = n_pol_counts

    singular_counter = Counter()
    for pair, count in pol_counts.items():
        for c in pair:
            singular_counter += {c: count}

    singular_counter += Counter([polymer[0], polymer[-1]])
    freq = singular_counter.most_common()
    return (freq[0][1] - freq[-1][1])//2

print(main(10))
print(main(40))