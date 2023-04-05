if __name__ == '__main__':
    text = input()

    line1 = '.'
    line2 = '.'
    line3 = '#'
    line4 = '.'
    line5 = '.'

    for index, t in enumerate(text, start=1):
        if(index % 3 == 0):
            line3 = ''.join(line3[0:-1])
            line1 += '.*..'
            line2 += '*.*.'
            line3 += f'*.{t}.*'
            line4 += '*.*.'
            line5 += '.*..'
        else:
            line1 += '.#..'
            line2 += '#.#.'
            line3 += f'.{t}.#'
            line4 += '#.#.'
            line5 += '.#..'
        
    for i in range(5):
        print(eval(f'line{i+1}'))