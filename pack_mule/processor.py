import pandas as pd


def lookup(val, xref):
    return xref[val]

def matcher(input_data):

    size_seq = dict(zip(input_data.get('size_sequence')['size'].values, input_data.get('size_sequence')['sequence'].values))
    color_xref = dict(zip(input_data.get('color_xref').input_color, input_data.get('color_xref').output_color))
    pack_data = [dict(zip(input_data['pack_input_data'].columns, r)) for r in input_data['pack_input_data'].values]

    for rw in pack_data:
        rw.update({
            'color_code': lookup(rw['color'], color_xref),
            'color_seq': list(color_xref.keys()).index(rw['color']) + 1,
            'size_seq': lookup(rw['size'], size_seq),
            'qty_size': '{}-{}'.format(str(rw['Units_In_Pack_ID']), rw['size'])
        })

    df = pd.DataFrame(pack_data)
    df['qty_size'] = df[['Pack_ID','color_code','qty_size']].groupby(['Pack_ID','color_code'])['qty_size'].transform(lambda x: '/'.join(x))
    df['config_string'] = df.apply(lambda x:'(%s: %s)' % (x['color_code'], x['qty_size']), axis=1)
    df['config_string'] = df[['Pack_ID','config_string']].groupby(['Pack_ID'])['config_string'].transform(lambda x: ''.join(x))

    return df.loc[:,['Pack_ID', 'config_string']].drop_duplicates()
