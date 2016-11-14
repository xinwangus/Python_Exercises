# excercise of use web api to acquire and analyse 
# data from web sites.

import requests
# need to do:
# pip3 install pygal
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
resp = requests.get(url)
print("status:", resp.status_code)
# now use json format
resp_dict = resp.json()

print("Total items:", resp_dict['total_count'])

if resp_dict['incomplete_results'] == False:
	print(resp_dict.keys())
	items_list = resp_dict['items']
	names = []
	stars = []
	#print(sorted(items_list[0].keys()))
	for item_dict in items_list[0:10]:
		names.append(item_dict['name'][0:3])
		stars.append(int(item_dict['stargazers_count']))
	print(names)
	print(stars)
	# map the chart
	#mystyle = LS('#333366', base_style=LCS)
	#chart = pygal.Bar(style=mystyle, x_label_rotation=45, show_legend=False)
	chart = pygal.Bar()
	chart.title = 'Most Starred Python Projects'

	chart.x_labels = names
	chart.add('Star count', stars)
	chart.render_to_file('bar.svg')

