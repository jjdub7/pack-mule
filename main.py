from pack_mule import config, reader, processor, writer

if __name__ == '__main__':
    print('Reading from input file...')
    input_data = reader.get_data(config.inputs.get('filename'))

    print('Running matching engine...')
    data = processor.matcher(input_data)

    print('Writing output file...')
    writer.write_out(data, config.output)

    print('Wrote data to {}.'.format(config.output.get('filename')))



