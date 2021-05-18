youtube-dl ha il flag -F (o --list-formats) per ottenere la lista dei formati disponibili. Non sono sempre gli stessi per ogni video e l'output è una cosa del tipo

401          mp4        3840x2160  2160p60 HDR 11707k , mp4_dash container, av01.0.13M.10.0.110.09.16.09.0@11707k, 60fps, video only, 437.93MiB
315          webm       3840x2160  2160p60 25573k , webm_dash container, vp9@25573k, 60fps, video only, 956.58MiB
701          mp4        3840x2160  2160p60 HDR 28033k , mp4_dash container, av01.0.13M.10.0.110.09.16.09.0@28033k, 60fps, video only, 1.02GiB
337          webm       3840x2160  2160p60 HDR 28869k , webm_dash container, vp9.2@28869k, 60fps, video only, 1.05GiB

dove la cosa importante è il video format code, il numero a inizio riga che corrisponde al formato


Per scaricare il formato giusto poi bisogna lanciare

youtube-dl -f <video format code> <url>