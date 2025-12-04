--
-- PostgreSQL database dump
--

\restrict XLWr8wgNhobhb9xpA24kmfQeTc7DB5M54CcUUZVcBmht7JCXgLffIGpfJVGuL7U

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_locatie; Type: TABLE DATA; Schema: django; Owner: victor
--



--
-- Name: magazin_locatie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_locatie_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict XLWr8wgNhobhb9xpA24kmfQeTc7DB5M54CcUUZVcBmht7JCXgLffIGpfJVGuL7U

--
-- PostgreSQL database dump
--

\restrict db5WjPMiX03vSAIDKYkmysDBhxrl55bjLtml3vrgrlbcx6jLVnrayQs3cph2HhR

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_animal; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (1, 'Mic', 'Câine', 'Yorkshire Terrier', 3.00, 'Necesită îngrijire regulată a blănii.');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (2, 'Mare', 'Câine', 'Ciobănesc German', 35.00, 'Blană de lungime medie, necesită periaj.');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (3, 'N/A', 'Pisică', 'Europeană (Comună)', 4.50, 'Blană scurtă, îngrijire minimă.');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (4, 'Mare', 'Pisică', 'Maine Coon', 8.00, 'Blană lungă, necesită periaj frecvent.');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (5, 'N/A', 'Pasăre', 'Papagal Jako', 0.40, 'Nu necesită servicii de tuns sau spălat.');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (6, 'Mic', 'Reptilă (Șopârlă)', 'Gecko Leopard', 0.08, 'Necesită terariu încălzit și substrat specific');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (7, 'Mare', 'Reptilă (Șopârlă)', 'Iguană Verde', 4.00, 'Necesită terariu mare, cu umiditate controlată și iluminare UVB puternică.');
INSERT INTO django.magazin_animal (id, dimensiune, specie, rasa, greutate, descriere) VALUES (8, 'Mediu', 'Reptilă (Țestoasă)', 'Broască Țestoasă de Florida (cu tâmple roșii)', 1.50, 'Semi-acvatică. Necesită acva-terariu cu filtru, încălzitor și lampă UV.');


--
-- Name: magazin_animale_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_animale_id_seq', 8, true);


--
-- PostgreSQL database dump complete
--

\unrestrict db5WjPMiX03vSAIDKYkmysDBhxrl55bjLtml3vrgrlbcx6jLVnrayQs3cph2HhR

--
-- PostgreSQL database dump
--

\restrict pR3KYMfN33uAda8veBXDAE1tqe1EjUzydWbufbItGdjHxKJ6syqtDEZcxFklAYB

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_categorie; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_categorie (id, denumire, descriere, slug, icon_class) VALUES (1, 'Hrană Uscată', 'Boabe și granule extrudate pentru câini, pisici și alte animale.', 'hrana-uscata', 'fa-solid fa-bone');
INSERT INTO django.magazin_categorie (id, denumire, descriere, slug, icon_class) VALUES (2, 'Hrană Umedă', 'Plicuri și conserve cu hrană în sos sau gelatină.', 'hrana-umeda', 'fa-solid fa-fish');
INSERT INTO django.magazin_categorie (id, denumire, descriere, slug, icon_class) VALUES (3, 'Accesorii și Jucării', 'Include lese, zgărzi, boluri, jucării din pluș, mingi și ansambluri de joacă.', 'accesorii-si-jucarii', 'fa-solid fa-baseball-ball');
INSERT INTO django.magazin_categorie (id, denumire, descriere, slug, icon_class) VALUES (4, 'Farmacie și Suplimente', 'Include produse de deparazitare, vitamine, suplimente pentru blană și articulații, șampoane medicale.', 'farmacie-si-suplimente', 'fa-solid fa-pills');
INSERT INTO django.magazin_categorie (id, denumire, descriere, slug, icon_class) VALUES (5, 'Igienă și Îngrijire', 'Include așternuturi igienice, nisip pentru pisici, perii, șampoane cosmetice și covorașe absorbante.', 'igiena-si-ingrijire', 'fa-solid fa-shower');


--
-- Name: magazin_categorii_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_categorii_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict pR3KYMfN33uAda8veBXDAE1tqe1EjUzydWbufbItGdjHxKJ6syqtDEZcxFklAYB

--
-- PostgreSQL database dump
--

\restrict rrtxgeLlnyp8lvJD1bhK2faEzCgkOnNPg76ea1vK57fWdNH2QW400ibdKt302v4

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_brand; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (1, 'Royal Canin', 'https://www.royalcanin.com/', '', '1968-01-01', 'Lider în nutriție științifică și diete veterinare. Oferă hrană super-premium adaptată nevoilor specifice ale rasei, vârstei și stării de sănătate a animalului.');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (2, 'Trixie', 'https://www.trixie.de/', '', '1974-01-01', 'Producător de top pentru accesorii, jucării, produse de îngrijire și transport. Nu produce hrană, concentrându-se pe echipamente non-alimentare.');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (3, 'Purina', 'https://www.purina.ro/', '', '1894-01-01', 'Brand global (parte din Nestlé) care produce o gamă largă, de la hrana comună (ex: Friskies) la diete veterinare specializate (ex: Pro Plan Veterinary Diets).');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (4, 'Hill''s Pet Nutrition', 'https://www.hillspet.ro/', '', '1907-01-01', 'Standardul industriei pentru hrana medicală (linia "Prescription Diet") și hrană premium bazată pe știință (linia "Science Plan").');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (5, 'Acana', 'https://acana.com/', '', '1979-01-01', 'Brand de top specializat în hrană "biologic apropiată", cu ingrediente proaspete, regionale și un conținut ridicat de carne (non-medicală).');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (6, 'Bravecto', 'https://www.bravecto.com/', '', '2011-01-01', 'Brand farmaceutic (MSD). Specializat în soluții de deparazitare (comprimate masticabile, pipete) cu acțiune de lungă durată împotriva puricilor și căpușelor.');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (7, 'Virbac', 'https://www.virbac.com/', '', '1968-01-01', 'Companie farmaceutică veterinară. Produce șampoane medicale, suplimente (vitamine), soluții de igienă dentară și alte produse farmaceutice.');
INSERT INTO django.magazin_brand (id, nume, website, logo, data_fond, descriere) VALUES (8, 'Foresto', 'https://www.elanco.com/', '', '2011-01-01', 'Brand farmaceutic (Elanco). Cunoscut pentru zgărzile antiparazitare de lungă durată (până la 8 luni) care protejează împotriva puricilor și căpușelor.');


--
-- Name: magazin_branduri_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_branduri_id_seq', 8, true);


--
-- PostgreSQL database dump complete
--

\unrestrict rrtxgeLlnyp8lvJD1bhK2faEzCgkOnNPg76ea1vK57fWdNH2QW400ibdKt302v4

--
-- PostgreSQL database dump
--

\restrict qafS6MDoulIW6gX4fHd5YP9xkYRVtuVpXx4T3IkfFOI4SXdGd0sYQe2SNPxvKXZ

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_furnizor; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_furnizor (id, nume_companie, email_contact, telefon, parteneri_din, note) VALUES (1, 'Zooplus AG', 'parteneri@zooplus.com', '+40 21 555 1020', '2018-01-15', 'Distribuitor general pentru diverse branduri internaționale.');
INSERT INTO django.magazin_furnizor (id, nume_companie, email_contact, telefon, parteneri_din, note) VALUES (2, 'MSD Animal Health Romania', 'office.romania@msd.com', '+40 21 333 4050', '2019-03-01', 'Furnizor principal pentru farmaceutice. Branduri cheie: Bravecto, Nobivac.');
INSERT INTO django.magazin_furnizor (id, nume_companie, email_contact, telefon, parteneri_din, note) VALUES (3, 'Elanco Romania', 'contact@elanco.com', '+40 31 888 7070', '2019-05-10', 'Furnizor farmaceutic. Branduri cheie: Foresto, Advantix.');
INSERT INTO django.magazin_furnizor (id, nume_companie, email_contact, telefon, parteneri_din, note) VALUES (4, 'Trixie Romania SRL', 'office@trixie.ro', '+40 26 444 9090', '2017-06-01', 'Furnizor principal pentru jucării, accesorii și produse non-alimentare.');
INSERT INTO django.magazin_furnizor (id, nume_companie, email_contact, telefon, parteneri_din, note) VALUES (5, 'Royal Canin Romania', 'contact.ro@royalcanin.com', '+40 21 222 5060', '2018-02-20', 'Furnizor direct pentru hrana super-premium și dietele veterinare Royal Canin.');


--
-- Name: magazin_furnizori_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_furnizori_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict qafS6MDoulIW6gX4fHd5YP9xkYRVtuVpXx4T3IkfFOI4SXdGd0sYQe2SNPxvKXZ

--
-- PostgreSQL database dump
--

\restrict lP9FgNCqMkqGsaHnhE7niO1eIqB1arg0LuCNKAV8TvcWUjkGopejYw6wyu449Ue

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_serviciu; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (1, 'Tuns Complet', 'Include tunsul blănii conform standardului rasei sau preferinței clientului, spălat și uscat.');
INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (2, 'Spălat și Igienizare', 'Include spălare cu șampon profesional, uscare cu prosopul și feonul, curățarea urechilor și tăierea unghiilor.');
INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (3, 'Periat și Descurcat Blană', 'Serviciu dedicat animalelor cu blană lungă sau medie, pentru eliminarea părului mort și descurcarea nodurilor.');
INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (5, 'Consultanță Nutrițională', 'Ședință de 30 de minute pentru stabilirea unei diete personalizate, adaptată nevoilor medicale, vârstei și rasei animalului.');
INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (6, 'Mentenanță Acvariu', 'Curățarea completă a acvariului, schimbarea parțială a apei, curățarea filtrelor și testarea parametrilor apei (pH, nitriți).');
INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (4, 'Cosmetică Unghii/Gheare', 'Serviciu rapid de tăiere și pilire a unghiilor/ghearelor');
INSERT INTO django.magazin_serviciu (id, nume, descriere) VALUES (7, 'Consultanță Habitate Exotice', 'Ședință de 30 de minute pentru setarea corectă a unui terariu sau acvariu (substrat, temperatură, umiditate, iluminare UV).');


--
-- Name: magazin_servicii_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_servicii_id_seq', 7, true);


--
-- PostgreSQL database dump complete
--

\unrestrict lP9FgNCqMkqGsaHnhE7niO1eIqB1arg0LuCNKAV8TvcWUjkGopejYw6wyu449Ue

--
-- PostgreSQL database dump
--

\restrict Tgv2wn5iAdihK8o3WEaoy4TSdgrQQ1pdGz86iqLfUJgQV589zSugOkf7jzQBnWJ

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_pret_serviciu; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (1, 130.00, 90, 1, 1);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (2, 250.00, 180, 2, 1);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (3, 140.00, 60, 2, 2);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (4, 170.00, 90, 4, 3);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (5, 60.00, 20, 3, 4);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (6, 90.00, 30, 7, 4);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (7, 200.00, 60, 6, 7);
INSERT INTO django.magazin_pret_serviciu (id, pret, durata, animal_id, serviciu_id) VALUES (8, 200.00, 60, 8, 6);


--
-- Name: magazin_preturi_servicii_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_preturi_servicii_id_seq', 8, true);


--
-- PostgreSQL database dump complete
--

\unrestrict Tgv2wn5iAdihK8o3WEaoy4TSdgrQQ1pdGz86iqLfUJgQV589zSugOkf7jzQBnWJ

--
-- PostgreSQL database dump
--

\restrict GBI6MrcNdRd4BIUMjwMua2mTuucpicM6DfnfyI4dAyIP3xPVJy4GajzoGqZARSl

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_produs; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (1, 'Royal Canin Maxi Adult', 'Hrană uscată completă pentru câini de talie mare (26-44kg), cu vârsta peste 15 luni.', 289.90, 30, '', '2025-11-04 10:33:30.969408+02', 1, 1, 15.000);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (2, 'Plic Purina Felix Sensations Jellies Vită', 'Hrană umedă (plic) cu bucăți fragede de vită într-un aspic suculent pentru pisici adulte.', 3.50, 300, '', '2025-11-04 11:36:31.232767+02', 3, 2, 0.100);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (3, 'Bravecto Comprimate Masticabile Antiparazitare', 'Potrivit pentru câini cu greutatea între 20-40 kg. Tratament eficient împotriva puricilor și căpușelor, cu acțiune prelungită de 12 săptămâni.', 145.00, 50, '', '2025-11-04 11:43:47.077709+02', 6, 4, 0.100);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (4, 'Zgardă Antiparazitară Foresto', 'Zgardă antiparazitară (70 cm). Potrivită pentru câini cu greutatea de peste 8 kg. Eficientă 8 luni împotriva puricilor și căpușelor. Rezistentă la apă.', 160.00, 45, '', '2025-11-04 11:48:41.532788+02', 8, 4, 0.050);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (6, 'Minge Trixie DentaFun', 'Minge de cauciuc natural (diametru 7cm) cu striații și aromă de mentă. Ajută la curățarea dinților și masarea gingiilor în timpul jocului.', 30.00, 120, '', '2025-11-04 11:52:03.604996+02', 2, 3, 0.150);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (5, 'Șampon Dermatologic Virbac Allermyl', 'Șampon calmant (200ml) pentru câini și pisici cu piele sensibilă, alergică sau iritată. Ajută la refacerea barierei cutanate.', 88.00, 25, '', '2025-11-04 11:49:54.621111+02', 7, 5, 0.200);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (7, 'Hill''s Diet Hrană Uscată Veterinară', 'Hrană uscată dietetică (sac 1.5kg), completă, pentru pisici diagnosticate cu afecțiuni renale. A se administra doar la recomandarea medicului veterinar.', 155.00, 15, '', '2025-11-04 11:55:36.034324+02', 4, 4, 1.500);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (8, 'Acana Classic Red', 'Hrană uscată "Biologically Appropriate" (sac 11.4kg) cu 50% carne (miel, vită Angus și porc Yorkshire). Fără cereale cu indice glicemic ridicat.', 265.00, 22, '', '2025-11-04 11:56:46.672652+02', 5, 1, 11.400);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (9, 'Bol Ceramic Trixie', 'Set două boluri ceramice albe (200ml fiecare) pe suport metalic negru, ușor înălțat. Ideal pentru pisici sau câini de talie mică.', 65.00, 40, '', '2025-11-04 11:59:18.87585+02', 2, 3, 0.750);
INSERT INTO django.magazin_produs (id, nume, descriere, pret, stoc, imagine, data_adaugarii, brand_id, categorie_id, greutate) VALUES (10, 'Conservă Hill''s Science Plan Câine Adult', 'Hrană umedă (conservă 370g) sub formă de pate, cu bucăți de pui. Nutriție echilibrată pentru câini adulți de talie medie (1-6 ani).', 12.50, 150, '', '2025-11-04 12:03:13.057664+02', 4, 2, 0.370);


--
-- Name: magazin_produse_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_produse_id_seq', 10, true);


--
-- PostgreSQL database dump complete
--

\unrestrict GBI6MrcNdRd4BIUMjwMua2mTuucpicM6DfnfyI4dAyIP3xPVJy4GajzoGqZARSl

--
-- PostgreSQL database dump
--

\restrict haqB1FJd21LMhr40cHbHR3VnjxtPSg7vUgd3OOqLHj2pTyxybeavzdRIOtHW9xU

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_oferta; Type: TABLE DATA; Schema: django; Owner: victor
--

INSERT INTO django.magazin_oferta (id, nume, data_inceput, data_sfarsit, reducere) VALUES (1, 'Săptămâna Hranei Umede', '2025-11-05', '2025-11-12', 15.00);
INSERT INTO django.magazin_oferta (id, nume, data_inceput, data_sfarsit, reducere) VALUES (2, 'Reducere Grooming de Iarnă', '2025-11-10', '2025-11-30', 25.00);
INSERT INTO django.magazin_oferta (id, nume, data_inceput, data_sfarsit, reducere) VALUES (3, 'Black Week Petshop', '2025-11-24', '2025-11-30', 25.00);


--
-- Name: magazin_oferte_id_seq; Type: SEQUENCE SET; Schema: django; Owner: victor
--

SELECT pg_catalog.setval('django.magazin_oferte_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict haqB1FJd21LMhr40cHbHR3VnjxtPSg7vUgd3OOqLHj2pTyxybeavzdRIOtHW9xU

