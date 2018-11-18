from LSB_audio import LSBAudio

if __name__ == '__main__':
    sound_path = 'gitar.wav'
    sound_steg_path = 'gitar_steg.wav'
    file_path = 'data.txt'
    output_path = 'data_steg.txt'
    num_lsb = 2
    bytes_to_recover = 9

    lsbAudio = LSBAudio()
    lsbAudio.hide_data(file_path, sound_path, sound_steg_path, num_lsb)
    lsbAudio.recover_data(sound_steg_path, output_path, num_lsb, bytes_to_recover)
