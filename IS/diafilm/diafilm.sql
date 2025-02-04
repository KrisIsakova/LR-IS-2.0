PGDMP  %                    |            diafilm    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    50392    diafilm    DATABASE     {   CREATE DATABASE diafilm WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE diafilm;
                postgres    false            �            1259    50408    diafilm    TABLE     t  CREATE TABLE public.diafilm (
    number integer NOT NULL,
    cipher text,
    cipher_2 text,
    cipher_3 text,
    year_on_the_title_card text,
    year_on_slide text,
    add_code text,
    "diafilm.su_1" text,
    "diafilm.su_2" text,
    box_with_label text,
    frame_link text,
    name text NOT NULL,
    copy "char" NOT NULL,
    note_1 text,
    note_2 text
);
    DROP TABLE public.diafilm;
       public         heap    postgres    false            �            1259    50407    diafilm_number_seq    SEQUENCE     �   CREATE SEQUENCE public.diafilm_number_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.diafilm_number_seq;
       public          postgres    false    216            �           0    0    diafilm_number_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.diafilm_number_seq OWNED BY public.diafilm.number;
          public          postgres    false    215            P           2604    50411    diafilm number    DEFAULT     p   ALTER TABLE ONLY public.diafilm ALTER COLUMN number SET DEFAULT nextval('public.diafilm_number_seq'::regclass);
 =   ALTER TABLE public.diafilm ALTER COLUMN number DROP DEFAULT;
       public          postgres    false    215    216    216            �          0    50408    diafilm 
   TABLE DATA           �   COPY public.diafilm (number, cipher, cipher_2, cipher_3, year_on_the_title_card, year_on_slide, add_code, "diafilm.su_1", "diafilm.su_2", box_with_label, frame_link, name, copy, note_1, note_2) FROM stdin;
    public          postgres    false    216          �           0    0    diafilm_number_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.diafilm_number_seq', 1, true);
          public          postgres    false    215            R           2606    50415    diafilm id_number 
   CONSTRAINT     S   ALTER TABLE ONLY public.diafilm
    ADD CONSTRAINT id_number PRIMARY KEY (number);
 ;   ALTER TABLE ONLY public.diafilm DROP CONSTRAINT id_number;
       public            postgres    false    216            �   +  x��WKr�F]O1���#d��<�vb:�T%��b���ƫTQaA�^a�Fy�� E2�\N���������u�Xe� T6KU��2��GW�r��O_��Kܮ�ԏ��q�����M��_�ܕ���ԕ�^�\�_�����v|�*�F�&�\�oq�	��ǉNf5�� �1,q��]�?�nX����h���5�M4=�WC��c?��\���v	���+m�eT} ���^��M�ٌ�s��w�;"ئW�N�W��>w��8����jX�;��_q��`�8VH��hGY*S�*VY���e��!�x(�%uB�X��j~�4�9�n�_�a���8[qZ)�m��G�&�0��4��a�t|<bW�)c�Le=��M
fnr���Α�[f�¿ڦ���6���9M�N�L���q�}@fȊ��PU�.0W��U�
��O��Y`���&2'y�y#��T\R��~Q�!�$�%�sU�_5�{*�
��V�Ӷ�v�w/�\t�����nY��S�f�f�QK�(��97~Ch�v��m���\���\�w@m-�#�A�}Cm�2Q�SJ�Q1��b�������+��q����
�D|²�	���zЭ���A�%�%�O�b��J�����DB�N����-O����4�p��d.�T���!@4�,�f��Q�&���:�(k�L�6:D�S���9�΁�yW�Hӆ���[�9��,9g{Yj�����_�f/m�V�����; ����Lrb)Ꝺ��0p[���-Sc3���y�
�t�
��ȕ��@EIH�Yu�k�ɪ(�=p�8����m��P�.e-5%蒜���V@dʤد��	�A��n��[����ЯhL����ѦJ/�k����a����b�ω����8>j%����Tz��-�gR�v0
K��l�T����*z/��
�����d���>1�U�2��}�y�Ϛ� �XE�i��U��U˓b�D
�[\h���`d��~W� �!��_��o�/���J�����ϵ�Ž�q�C�_h���١�O:��ߒxA�     