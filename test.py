import pstats
p = pstats.Stats('output_file.log')
p.sort_stats('cumulative').print_stats()