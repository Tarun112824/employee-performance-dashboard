# Uses ReportLab/Matplotlib
def generate_top_performers_pdf(df):
    plt.bar(df['name'], df['score'])
    plt.savefig('report.png')  # Embed in PDF