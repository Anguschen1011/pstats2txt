import io
import pstats


profile_results_file = 'profile_results.pstats'
txt_path = 'profile_results.txt'

s = io.StringIO()
stats = pstats.Stats(profile_results_file, stream=s)
stats.print_stats()

with open(txt_path, 'w+') as f:
    f.write(s.getvalue())