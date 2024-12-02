import mapel.roommates as mapel
import random
import math

size = 0
num_agents = 6

def add_ti(list, incomplete_percent, ties_percent):
    agents_to_remove = int(len(list) * incomplete_percent)
    ties_to_add = int((len(list)-1) * ties_percent)

    for i in range(len(list)):
        sample = random.sample(range(len(list)-1), agents_to_remove)
        sample.sort(reverse=True)
        for s in sample:
            list[i].pop(s)
            list[i].append([])

    for i in range(len(list)):
        sample = random.sample(range(1, len(list)-1), ties_to_add)
        sample.sort(reverse=True)
        for idx in sample:
            for ag in list[i][idx]:
                list[i][idx-1].append(ag)

            list[i].pop(idx)
            list[i].append([])
    return list

experiment = mapel.prepare_online_roommates_experiment()

# experiment.add_instance(culture_id='fully_incomplete',
#                         label='Empty',
#                         num_agents=num_agents,
#                         color='green', marker='+', ms = 125)
# experiment.add_instance(culture_id='fully_tied',
#                         label='Ties',
#                         num_agents=num_agents,
#                         color='purple', marker='+', ms = 125)
# experiment.add_instance(culture_id='id',
#                         label='ID',
#                         num_agents=num_agents,
#                         color='red', marker='+', ms = 125)
# experiment.add_instance(culture_id='symmetric',
#                         label='MA',
#                         num_agents=num_agents,
#                         color='orange', marker='+', ms = 125)
# experiment.add_instance(culture_id='asymmetric',
#                         label='MD',
#                         num_agents=num_agents,
#                         color='blue', marker='+', ms = 125)
experiment.add_instance(culture_id='chaos',
                        label='CH',
                        num_agents=num_agents,
                        color='black', marker='+', ms = 125)
    

sr_families = [
    { 'culture': 'expectation', 'label': 'Expectation_0.2', 'params': {'std': .2}, 'color': 'red', 'marker': 'o' },
    { 'culture': 'expectation', 'label': 'Expectation_0.4', 'params': {'std': .4}, 'color': 'red', 'marker': 'o' },

    { 'culture': 'ic', 'label': 'Impartial', 'params': {}, 'color': 'magenta', 'marker': 'o' },

    { 'culture': 'group_ic', 'label': 'Group_ic_0.25', 'params': {'proportion': 0.25}, 'color': 'darkviolet', 'marker': 'o' },
    { 'culture': 'group_ic', 'label': 'Group_ic_0.50', 'params': {'proportion': 0.50}, 'color': 'darkviolet', 'marker': 'o' },

    { 'culture': 'attributes', 'label': 'Attributes_2D', 'params': {'dim': 2}, 'color': 'yellow', 'marker': 'o' },
    { 'culture': 'attributes', 'label': 'Attributes_5D', 'params': {'dim': 5}, 'color': 'yellow', 'marker': 'o' },

    { 'culture': 'fame', 'label': 'Fame_0.2', 'params': {'radius': .2}, 'color': 'lime', 'marker': 'o' },
    { 'culture': 'fame', 'label': 'Fame_0.4', 'params': {'radius': .4}, 'color': 'lime', 'marker': 'o' },

    { 'culture': 'reverse_euclidean', 'label': 'Reverse_euclidean_0.05', 'params': {'proportion': .05}, 'color': 'sienna', 'marker': 'o' },
    { 'culture': 'reverse_euclidean', 'label': 'Reverse_euclidean_0.15', 'params': {'proportion': .15}, 'color': 'sienna', 'marker': 'o' },
    { 'culture': 'reverse_euclidean', 'label': 'Reverse_euclidean_0.25', 'params': {'proportion': .25}, 'color': 'sienna', 'marker': 'o' },

    { 'culture': 'mallows_euclidean', 'label': 'Mallows_euclidean_0.2', 'params': {'phi': .2}, 'color': 'cyan', 'marker': 'o' },
    { 'culture': 'mallows_euclidean', 'label': 'Mallows_euclidean_0.4', 'params': {'phi': .4}, 'color': 'cyan', 'marker': 'o' },
    { 'culture': 'mallows_euclidean', 'label': 'Mallows_euclidean_0.6', 'params': {'phi': .6}, 'color': 'cyan', 'marker': 'o' },

    { 'culture': 'norm-mallows', 'label': 'Norm_mallows_0.2', 'params': {'normphi': .2}, 'color': 'green', 'marker': 'o' },
    { 'culture': 'norm-mallows', 'label': 'Norm_mallows_0.4', 'params': {'normphi': .4}, 'color': 'green', 'marker': 'o' },
    { 'culture': 'norm-mallows', 'label': 'Norm_mallows_0.6', 'params': {'normphi': .6}, 'color': 'green', 'marker': 'o' },
    { 'culture': 'norm-mallows', 'label': 'Norm_mallows_0.8', 'params': {'normphi': .8}, 'color': 'green', 'marker': 'o' },

    { 'culture': 'malasym', 'label': 'Mallows_md_0.2', 'params': {'normphi': .2}, 'color': 'blue', 'marker': 'o' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.4', 'params': {'normphi': .4}, 'color': 'blue', 'marker': 'o' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.6', 'params': {'normphi': .6}, 'color': 'blue', 'marker': 'o' },
] # 22 cultures

srti_families = [
    # Ties
    { 'culture': 'expectation', 'label': 'Expectation_0.2(00, 25)', 'params': {'srti_func': add_ti, 'incompleteness': .00, 'ties': .25, 'std': .2}, 'color': 'red', 'marker': 'o' },
    { 'culture': 'expectation', 'label': 'Expectation_0.2(00, 50)', 'params': {'srti_func': add_ti, 'incompleteness': .00, 'ties': .50, 'std': .2}, 'color': 'red', 'marker': 'o' },
    { 'culture': 'expectation', 'label': 'Expectation_0.2(00, 75)', 'params': {'srti_func': add_ti, 'incompleteness': .00, 'ties': .75, 'std': .2}, 'color': 'red', 'marker': 'o' },
    # Incompleteness
    { 'culture': 'expectation', 'label': 'Expectation_0.2(25, 00)', 'params': {'srti_func': add_ti, 'incompleteness': .25, 'ties': .00, 'std': .2}, 'color': 'red', 'marker': 's' },
    { 'culture': 'expectation', 'label': 'Expectation_0.2(50, 00)', 'params': {'srti_func': add_ti, 'incompleteness': .50, 'ties': .00, 'std': .2}, 'color': 'red', 'marker': 's' },
    { 'culture': 'expectation', 'label': 'Expectation_0.2(75, 00)', 'params': {'srti_func': add_ti, 'incompleteness': .75, 'ties': .00, 'std': .2}, 'color': 'red', 'marker': 's' },
    # Mixed
    { 'culture': 'expectation', 'label': 'Expectation_0.2(25, 25)', 'params': {'srti_func': add_ti, 'incompleteness': .25, 'ties': .25, 'std': .2}, 'color': 'red', 'marker': 'd' },
    { 'culture': 'expectation', 'label': 'Expectation_0.2(50, 50)', 'params': {'srti_func': add_ti, 'incompleteness': .50, 'ties': .50, 'std': .2}, 'color': 'red', 'marker': 'd' },
    { 'culture': 'expectation', 'label': 'Expectation_0.2(75, 75)', 'params': {'srti_func': add_ti, 'incompleteness': .75, 'ties': .75, 'std': .2}, 'color': 'red', 'marker': 'd' },

    # Ties
    { 'culture': 'euclidean', 'label': 'Euclidean(00, 25)', 'params': {'srti_func': add_ti, 'incompleteness': .00, 'ties': .25}, 'color': 'lightcoral', 'marker': 'o' }, 
    { 'culture': 'euclidean', 'label': 'Euclidean(00, 50)', 'params': {'srti_func': add_ti, 'incompleteness': .00, 'ties': .50}, 'color': 'lightcoral', 'marker': 'o' },
    { 'culture': 'euclidean', 'label': 'Euclidean(00, 75)', 'params': {'srti_func': add_ti, 'incompleteness': .00, 'ties': .75}, 'color': 'lightcoral', 'marker': 'o' },
    # Incompleteness
    { 'culture': 'euclidean', 'label': 'Euclidean(25, 00)', 'params': {'srti_func': add_ti, 'incompleteness': .25, 'ties': .00}, 'color': 'lightcoral', 'marker': 's' },
    { 'culture': 'euclidean', 'label': 'Euclidean(50, 00)', 'params': {'srti_func': add_ti, 'incompleteness': .50, 'ties': .00}, 'color': 'lightcoral', 'marker': 's' },
    { 'culture': 'euclidean', 'label': 'Euclidean(75, 00)', 'params': {'srti_func': add_ti, 'incompleteness': .75, 'ties': .00}, 'color': 'lightcoral', 'marker': 's' },
    # Mixed
    { 'culture': 'euclidean', 'label': 'Euclidean(25, 25)', 'params': {'srti_func': add_ti, 'incompleteness': .25, 'ties': .25}, 'color': 'lightcoral', 'marker': 'd' },
    { 'culture': 'euclidean', 'label': 'Euclidean(50, 50)', 'params': {'srti_func': add_ti, 'incompleteness': .50, 'ties': .50}, 'color': 'lightcoral', 'marker': 'd' },
    { 'culture': 'euclidean', 'label': 'Euclidean(75, 75)', 'params': {'srti_func': add_ti, 'incompleteness': .75, 'ties': .75}, 'color': 'lightcoral', 'marker': 'd' },

    # Ties
    { 'culture': 'malasym', 'label': 'Mallows_md_0.2(00, 25)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .25, 'normphi': .2}, 'color': 'blue', 'marker': 'o' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.2(00, 50)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .50, 'normphi': .2}, 'color': 'blue', 'marker': 'o' },
    # Incompleteness
    { 'culture': 'malasym', 'label': 'Mallows_md_0.2(25, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .25, 'ties': .00, 'normphi': .2}, 'color': 'blue', 'marker': 'o' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.2(50, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .50, 'ties': .00, 'normphi': .2}, 'color': 'blue', 'marker': 'o' },
    
    # Ties
    { 'culture': 'malasym', 'label': 'Mallows_md_0.4(00, 25)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .25, 'normphi': .4}, 'color': 'blue', 'marker': 's' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.4(00, 50)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .50, 'normphi': .4}, 'color': 'blue', 'marker': 's' },
    # Incompleteness
    { 'culture': 'malasym', 'label': 'Mallows_md_0.4(25, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .25, 'ties': .00, 'normphi': .4}, 'color': 'blue', 'marker': 's' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.4(50, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .50, 'ties': .00, 'normphi': .4}, 'color': 'blue', 'marker': 's' },

    # Ties
    { 'culture': 'malasym', 'label': 'Mallows_md_0.6(00, 25)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .25, 'normphi': .6}, 'color': 'blue', 'marker': 'd' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.6(00, 50)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .50, 'normphi': .6}, 'color': 'blue', 'marker': 'd' },
    # Incompleteness
    { 'culture': 'malasym', 'label': 'Mallows_md_0.6(25, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .25, 'ties': .00, 'normphi': .6}, 'color': 'blue', 'marker': 'd' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.6(50, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .50, 'ties': .00, 'normphi': .6}, 'color': 'blue', 'marker': 'd' },
    
    # Ties
    { 'culture': 'malasym', 'label': 'Mallows_md_0.8(00, 25)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .25, 'normphi': .8}, 'color': 'blue', 'marker': '*' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.8(00, 50)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .50, 'normphi': .8}, 'color': 'blue', 'marker': '*' },
    # Incompleteness
    { 'culture': 'malasym', 'label': 'Mallows_md_0.8(25, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .25, 'ties': .00, 'normphi': .8}, 'color': 'blue', 'marker': '*' },
    { 'culture': 'malasym', 'label': 'Mallows_md_0.8(50, 00)', 'params': { 'srti_func': add_ti, 'incompleteness': .50, 'ties': .00, 'normphi': .8}, 'color': 'blue', 'marker': '*' },

    # Mixed
    { 'culture': 'malasym', 'label': 'Mallows_md_0.2(00, 25)', 'params': { 'srti_func': add_ti, 'incompleteness': .00, 'ties': .25, 'normphi': .2}, 'color': 'blue', 'marker': 'o' },


] # 35 cultures

# for family in srti_families:
#     experiment.add_family(culture_id=family['culture'],
#                         family_id=family['label'],
#                         label=family['label'],
#                         params=family['params'],
#                         num_agents=num_agents, size=size,
#                         color=family['color'], marker=family['marker'])

# for family in sr_families:
#     experiment.add_family(culture_id=family['culture'],
#                             family_id=family['label'],
#                             label=family['label'],
#                             params=family['params'],
#                             num_agents=num_agents, size=size,
#                             color=family['color'], marker=family['marker'])


textual = ['Empty', 'Ties', 'ID', 'MD', 'MA', 'CH']
figsize = (8,8)

saveas = 'otherstuff'
experiment.compute_distances(distance_id='mutual_attraction', num_threads=5)
experiment.embed_2d(embedding_id='kk')

# experiment.print_map_2d(show=False, textual=textual, saveas=saveas, legend_pos=(0,0), figsize=figsize)

# for family in sr_families:
#     save_name = family['label'].replace('.', '').replace(',', '')
#     experiment.print_map_2d(show=False, textual=[family['label']], saveas=save_name, legend=False, figsize=figsize)
# for family in srti_families:
#     save_name = family['label'].replace('.', '').replace(',', '')
#     experiment.print_map_2d(show=False, textual=[family['label']], saveas=save_name, legend=False, figsize=figsize)

# mallows_md_families = [fam['label'] for fam in srti_families if fam['culture'] == 'malasym']
# experiment.print_map_2d(show=False, textual=mallows_md_families, saveas='mallows_md_highlighted', legend=False, figsize=figsize)
# euclidean_families = [fam['label'] for fam in srti_families if fam['culture'] == 'euclidean']
# experiment.print_map_2d(show=False, textual=euclidean_families, saveas='euclidean_highlighted', legend=False, figsize=figsize)
# expectation_families = [fam['label'] for fam in srti_families if fam['culture'] == 'expectation']
# experiment.print_map_2d(show=False, textual=expectation_families, saveas='expectation_highlighted', legend=False, figsize=figsize)

# experiment.compute_feature(feature_id='number_of_solutions')
# experiment.compute_feature(feature_id='dist_from_id_1')
# experiment.compute_feature(feature_id='mutuality')
# experiment.compute_feature(feature_id='min_num_bps_matching')
# experiment.compute_feature(feature_id='avg_num_of_bps_for_rand_matching')
# experiment.compute_feature(feature_id='num_of_bps_min_weight')

# experiment.print_map_2d_colored_by_feature(show=False, textual=textual, feature_id='number_of_solutions', saveas=saveas+'_numsolutions', figsize=figsize, scale='log')
# experiment.print_map_2d_colored_by_feature(show=False, textual=textual, rounding=0, feature_id='dist_from_id_1', saveas=saveas+'_rankdistortion', figsize=figsize)
# experiment.print_map_2d_colored_by_feature(show=False, textual=textual, rounding=0, feature_id='mutuality', saveas=saveas+'_mutuality', figsize=figsize)
# experiment.print_map_2d_colored_by_feature(show=False, textual=textual, rounding=0, feature_id='min_num_bps_matching', saveas=saveas+'_minbps', figsize=figsize)
# experiment.print_map_2d_colored_by_feature(show=False, textual=textual, rounding=0, feature_id='avg_num_of_bps_for_rand_matching', saveas=saveas+'_avgbps', figsize=figsize)
# experiment.print_map_2d_colored_by_feature(show=False, textual=textual, rounding=0, feature_id='num_of_bps_min_weight', saveas=saveas+'_numbps_minweight', figsize=figsize, scale='log')
