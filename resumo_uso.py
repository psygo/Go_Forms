columns = ['timestamp',
           'nome',
           'idade',
           'nivel',
           'exp',
           'perc_temp',
           'go_rank',
           'cidade',
           'servidor',
           'horario',
           'lingua',
           'go_educ',
           'go_expec',
           'livros',
           'int_desloc',
           'int_desloc_dia',
           'int_desloc_loc',
           'int_desloc_tempo',
           'tempo_videos',
           'int_aulas',
           'int_aulas_valor',
           'importancia',
           'esporte',
           'int_comp',
           'ibero',
           'sugestoes']
           
# Pie

sizes = f.pie_sizes(df, 'go_educ')

f.plot_pie(sizes = sizes,
           figsize = size_pie,
           title = 'Força',
           fontsize = title_font_size,
           path_img = path_img,
           file_name = 'pie_forca.jpg',
           dpi = dpi)

# Hist

stepper, bars = f.normed_hist(df['exp'], bins)

idade = df['idade']
idade_mean = idade.mean()

'Média de Idade: {round(idade_mean, 2)}'

f.plot_normed_hist(stepper,
                   bars,
                   figsize = figsize,
                   xlabel = 'idade',
                   ylabel = '%',
                   title = 'Histograma de Idades',
                   fontsize = title_font_size,
                   path_img = path_img,
                   file_name = 'hist_idade.jpg',
                   dpi = dpi)

# Hist Mult

s, l = f.split_unique_plus_stats(df, 'servidor')

f.plot_sups(size_figure = figsize,
            s = s, l = l,
            xlabel = '%',
            ylabel = 'Horário de Jogo',
            title = 'Horário de Jogo',
            title_font_size = title_font_size,
            path = path_img,
            file_name = 'mult_hist_horario.jpg')