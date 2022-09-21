
def write_out(data, config):

    data.to_csv(path_or_buf=config.get('filename'), index=False)

    # with open(config.get('filename'), 'w', encoding='UTF8', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(config.get('header'))
    #
    #     for rw in data:
    #         writer.writerow()
