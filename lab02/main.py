from utils import retrieve_data, process_data
import lab_3_a, lab_3_b, lab_3_c, lab_3_d, lab_3_e, lab_3_f, lab_3_g, lab_3_h


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    
    # funkcje redukujące
    print("Liczba żądań z kodem 200: ", end="")
    print(lab_3_a.reduce_request(data, "200"))
    print("Liczba żądań z kodem 302: ", end="")
    print(lab_3_a.reduce_request(data, "302"))
    print("Liczba żądań z kodem 404: ", end="")
    print(lab_3_a.reduce_request(data, "404"))
    print("Sumaryczna liczba danych wysłanych do hostów w GB: ", end="\t")
    print(f"{lab_3_b.reduce_resource_size(data)} GB")
    print("Ścieżka i rozmiar (w B) największego zasobu: ", end="\t\t")
    print(lab_3_c.reduce_largest_resource(data))
    print("Stosunek pobrań grafiki do pozostałych zasobów: ", end="\t")
    print(lab_3_d.reduce_image_ratio(data))
    
    # funkcje filtrujące (zakomentowane, bo wypisują strasznie dużo danych)
    """ print("Żądania z kodem odpowiedzi 200:")
    print(*lab_3_e.filter_requests(data))
    print("Zasoby pobierane pomiędzy 22 a 6 rano:")
    print(*lab_3_f.filter_download_time(data))
    print("Zasoby pobierane w piątek:")
    print(*lab_3_g.filter_download_date(data))
    print("Żądania z Polski (hostów z domeną zakończoną na .pl):")
    print(*lab_3_h.filter_download_location(data)) """