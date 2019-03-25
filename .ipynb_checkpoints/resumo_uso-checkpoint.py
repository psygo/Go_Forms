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

nivel = df['nivel']

nivel_sizes = nivel.value_counts() / nivel.count()

explode = tuple([0.05 for _ in range(0, len(nivel_sizes))])

plt.figure(figsize = size_pie)
plt.pie(nivel_sizes, labels = nivel_sizes.index, autopct='%1.1f%%')
plt.title('Força', fontsize = title_font_size)
plt.savefig(path_img + 'forca.jpg', dpi = dpi)
plt.show()

# Hist

stepper, bars = f.normed_hist(df['exp'], bins)

plt.figure(figsize = figsize)
plt.bar(stepper, height = bars * 100)
plt.xlabel('anos de jogo')
plt.ylabel('%')
plt.title('Histograma de Experiência', fontsize = title_font_size)
plt.savefig(path_img + 'hist_exp.jpg', dpi = dpi)
plt.show()

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