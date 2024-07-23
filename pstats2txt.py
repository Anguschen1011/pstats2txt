import pstats
import io

profile_results_file = '/Users/anguschen/Project/FashionTex/profile_results.pstats'
write_path = '/Users/anguschen/Project/FashionTex/profile_results.txt'

s = io.StringIO()
stats = pstats.Stats(profile_results_file, stream=s)
stats.print_stats()

with open(write_path, 'w+') as f:
    f.write(s.getvalue())