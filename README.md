# Enkriptimi-Dekriptimi3DES

 3DES Encryption Tool
Ky projekt ofron një mjet të thjeshtë në Python për enkriptimin dhe dekriptimin e të dhënave (tekst dhe fajlla) duke përdorur algoritmin simetrik Triple DES (3DES) në modalitetin CBC (Cipher Block Chaining).

 Si funksionon?
Programi përdor bibliotekën pycryptodome për të kryer operacionet kriptografike:

Enkriptimi (Tekst/Fajll):

Gjenerohet një IV (Initialization Vector) unik për çdo sesion enkriptimi për të siguruar siguri më të lartë.

Të dhënat i nënshtrohen Padding (PKCS7) për të përmbushur kërkesat e gjatësisë së bllokut të 3DES.

Për tekstin, rezultati konvertohet në Base64 për ta bërë të lehtë për t'u kopjuar/shfaqur.

Dekriptimi:

Programi lexon IV-në nga fillimi i të dhënave të enkriptuara.

Përdor IV-në dhe çelësin statik për të kthyer të dhënat në gjendjen origjinale.

Aplikon Unpadding për të hequr mbushjen shtesë dhe për të kthyer tekstin/fajllin në formatin fillestar.

 Shënime për sigurinë
Çelësi (KEY): Aktualisht përdoret një çelës statik (hardcoded) për qëllime edukative. Në një mjedis real, çelësat duhet të gjenerohen në mënyrë të rastësishme dhe të ruhen në mënyrë të sigurt.

Algoritmi: 3DES konsiderohet një algoritmi i vjetëruar nga standardet moderne (rekomandohet AES për projekte të reja), por mbetet një shembull i shkëlqyer për të kuptuar bazat e kriptografisë simetrike.
