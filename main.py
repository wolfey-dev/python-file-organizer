import os
import configparser
import argparse

file_extensions = {
    "Pictures": [".png", ".jpg", ".jpeg", ".jpe", ".jfif", ".pjpeg", ".pjp", ".webp", ".avif", ".apng", ".gif", ".jxl", ".svg", ".bmp", ".dib", ".ico", ".cur", ".tif", ".tiff", ".heic", ".heif", ".heics", ".heifs", ".hif", ".raw", ".cr2", ".cr3", ".crw", ".nef", ".nrw", ".arw", ".srf", ".sr2", ".dng", ".raf", ".orf", ".rw2", ".pef", ".ptx", ".3fr", ".ari", ".bay", ".cap", ".dcs", ".dcr", ".drf", ".eip", ".erf", ".fff", ".gpr", ".iiq", ".k25", ".kdc", ".mdc", ".mef", ".mos", ".mrw", ".obm", ".pxn", ".rwl", ".rwz", ".x3f", ".psd", ".psb", ".xcf", ".afphoto", ".afdesign", ".ai", ".eps", ".ps", ".pdf", ".indd", ".idml", ".exr", ".hdr", ".pic", ".pict", ".pct", ".sgi", ".rgb", ".rgba", ".bw", ".ras", ".sun", ".tga", ".icb", ".vda", ".vst", ".dds", ".ktx", ".ktx2", ".basis", ".pvr", ".astc", ".jng", ".mng", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".jng", ".hdp", ".wdp", ".jxr", ".flif", ".bpg", ".qoi", ".pbm", ".pgm", ".ppm", ".pnm", ".pam", ".pfm", ".xbm", ".xpm", ".pcx", ".dcx", ".iff", ".ilbm", ".lbm", ".mac", ".msp", ".cut", ".jif", ".emf", ".wmf", ".cgm", ".dcm", ".dicom", ".fits", ".fit", ".fts", ".ecw", ".sid", ".jp2", ".j2c", ".jpc", ".jpf", ".jpx", ".jpm", ".jng", ".cur", ".ani"],
    "Videos": [".webm", ".mkv", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gifv", ".mng", ".avi", ".mts", ".m2ts", ".ts", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".viv", ".asf", ".amv", ".mp4", ".m4p", ".m4v", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".m2v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".f4v", ".f4p", ".f4a", ".f4b", ".m2t", ".m2p", ".m2v", ".m2a", ".m2s", ".m2ts", ".m2v", ".m4v", ".mkv", ".mk3d", ".mka", ".mks", ".mp4v", ".mp4", ".mpeg4", ".mpg4", ".m1v", ".m2v", ".m4v", ".mpe", ".mpeg", ".mpg", ".mpv2", ".m2p", ".m2t", ".m2ts", ".m2v", ".m2a", ".m2s", ".3gpp", ".3gpp2", ".3gp2", ".3g2", ".3gpp", ".dv", ".dif", ".f4v", ".flv", ".h264", ".264", ".hevc", ".h265", ".265", ".ivf", ".mjpeg", ".mjpg", ".mj2", ".mjp2", ".nut", ".nuv", ".ogm", ".ogx", ".ps", ".rec", ".tod", ".trp", ".tp", ".wtv", ".webm", ".y4m", ".bik", ".bk2", ".smk", ".roq", ".r3d", ".cine", ".ismv", ".ism", ".mpd", ".m3u8", ".m3u", ".f4m", ".ismc", ".amv", ".cam", ".dat", ".divx", ".evo", ".ivf", ".mod", ".tod", ".vro", ".rec", ".vp6", ".vp7", ".vp8", ".vp9", ".av1", ".m1v", ".m2v", ".m4s", ".264", ".265"],
    "Documents": [".txt", ".text", ".rtf", ".doc", ".docx", ".docm", ".dot", ".dotx", ".dotm", ".odt", ".fodt", ".ott", ".sxw", ".wp", ".wpd", ".wp7", ".wps", ".wpt", ".pages", ".abw", ".zabw", ".lwp", ".602", ".hwp", ".hwpx", ".odm", ".pmd", ".p65", ".qxd", ".qxp", ".pub", ".pwi", ".one", ".onepkg", ".guide", ".md", ".markdown", ".mdown", ".mkd", ".rst", ".asciidoc", ".adoc", ".tex", ".latex", ".ltx", ".bib", ".cls", ".sty", ".dtx", ".ins", ".pdf", ".pdfa", ".xps", ".oxps", ".djv", ".djvu", ".ps", ".eps", ".dvi", ".pcl", ".prn", ".xml", ".html", ".htm", ".xhtml", ".mhtml", ".mht", ".shtml", ".sgml", ".dita", ".ditamap", ".docbook", ".dbk", ".fb2", ".fb3", ".epub", ".mobi", ".azw", ".azw3", ".azw4", ".kfx", ".kf8", ".pdb", ".prc", ".lit", ".lrf", ".lrx", ".cbz", ".cbr", ".cb7", ".cbt", ".chm", ".opf", ".uof", ".uot", ".uos", ".uop", ".sxc", ".sxd", ".sxi", ".odg", ".otg", ".odp", ".otp", ".ods", ".ots", ".slk", ".xls", ".xlt", ".xlm", ".xlsx", ".xlsm", ".xltx", ".xltm", ".xlsb", ".xla", ".xlam", ".xll", ".xlw", ".xll_", ".csv", ".tsv", ".dif", ".numbers", ".fods", ".wbk", ".wil", ".wwl", ".tmac", ".man", ".info", ".nfo", ".rtfd", ".icml", ".indd", ".idml", ".vsd", ".vsdx", ".vssx", ".vstx", ".drawio", ".odc", ".odf", ".stw", ".vor", ".sxg", ".cwk", ".cwkz", ".qbw", ".qbb", ".qbx"],
    "Music": [".mp3", ".wav", ".wave", ".flac", ".alac", ".aiff", ".aif", ".aifc", ".aac", ".m4a", ".m4b", ".m4p", ".m4r", ".ogg", ".oga", ".opus", ".wma", ".mid", ".midi", ".kar", ".mp2", ".mp1", ".mpa", ".mpc", ".mpp", ".mp+", ".ape", ".wv", ".tta", ".tak", ".ofr", ".ofs", ".spx", ".gsm", ".amr", ".awb", ".au", ".snd", ".raw", ".pcm", ".caf", ".voc", ".8svx", ".svx", ".ircam", ".sf", ".sd2", ".dss", ".dsf", ".dff", ".ast", ".ac3", ".eac3", ".ec3", ".dts", ".dtshd", ".mlp", ".thd", ".truehd", ".ra", ".ram", ".rm", ".mid", ".midi", ".rmi", ".mod", ".xm", ".s3m", ".it", ".mptm", ".mt2", ".umx", ".669", ".amf", ".ams", ".dbm", ".digi", ".dmf", ".dsm", ".far", ".gdm", ".imf", ".j2b", ".m15", ".med", ".mms", ".okt", ".pt36", ".ptm", ".sfx", ".stm", ".stp", ".ult", ".wow", ".wve", ".mus", ".musicxml", ".mxl", ".abc", ".ly", ".lilypond", ".gp", ".gp3", ".gp4", ".gp5", ".gpx", ".gpt", ".mscz", ".mscx", ".sib", ".mid", ".midi", ".kar", ".rtttl", ".hmi", ".hmp", ".xmi", ".lds", ".opb", ".opus"],
    "Scripts": [".sh", ".bash", ".zsh", ".fish", ".ksh", ".csh", ".tcsh", ".ps1", ".psm1", ".psd1", ".ps1xml", ".bat", ".cmd", ".btm", ".vbs", ".vbe", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".py", ".pyw", ".pyc", ".pyo", ".pyd", ".rb", ".rbw", ".pl", ".pm", ".t", ".php", ".phar", ".phtml", ".asp", ".aspx", ".jsp", ".cfm", ".cfc", ".lua", ".luac", ".r", ".rmd", ".jl", ".groovy", ".gvy", ".gy", ".gsh", ".java", ".class", ".scala", ".sc", ".clj", ".cljs", ".cljc", ".edn", ".ex", ".exs", ".erl", ".hrl", ".hrb", ".hs", ".lhs", ".elm", ".dart", ".swift", ".applescript", ".scpt", ".workflow", ".action", ".command", ".desktop", ".appref-ms", ".wsf", ".wsh", ".hta", ".jse", ".sct", ".ws", ".wsd", ".reg", ".inf", ".au3", ".a3x", ".ahk", ".ah2", ".v", ".vim", ".vimrc", ".nvim", ".el", ".lisp", ".lsp", ".scm", ".ss", ".rkt", ".tcl", ".tk", ".awk", ".sed", ".m4", ".make", ".mk", ".mak", ".cmake", ".gradle", ".gradle.kts", ".nsi", ".nsh", ".iss", ".pas", ".pp", ".dpr", ".prg", ".p", ".sql", ".mysql", ".pgsql", ".psql", ".plsql", ".ddl", ".dml", ".graphql", ".gql", ".proto", ".thrift", ".ipynb", ".nb", ".wl", ".wls", ".mat", ".mlx", ".m", ".oct", ".sas", ".do", ".ado", ".rpy", ".renpy", ".godot", ".gd", ".gdc", ".csx", ".fsx", ".vbs", ".vba", ".bas", ".cls", ".frm", ".frx", ".xlam", ".xla", ".wasm", ".wat", ".asm", ".s", ".inc", ".nasm", ".pl", ".pro", ".pde", ".ino", ".hlsl", ".glsl", ".vert", ".frag", ".geom", ".tesc", ".tese", ".comp"],
    "Executables": [".exe", ".com", ".msi", ".msp", ".mst", ".msix", ".appx", ".appxbundle", ".msixbundle", ".app", ".dmg", ".pkg", ".mpkg", ".deb", ".rpm", ".apk", ".aab", ".apks", ".xapk", ".ipa", ".jar", ".war", ".ear", ".class", ".bin", ".elf", ".out", ".run", ".sh", ".bash", ".command", ".bat", ".cmd", ".ps1", ".psm1", ".psd1", ".scr", ".pif", ".hta", ".cpl", ".sys", ".drv", ".ocx", ".dll", ".so", ".dylib", ".framework", ".bundle", ".appimage", ".flatpak", ".snap", ".portable", ".appref-ms", ".gadget", ".vbs", ".vbe", ".js", ".jse", ".wsf", ".wsh", ".msc", ".reg", ".inf", ".iso", ".img", ".vhd", ".vhdx", ".vmdk", ".vdi", ".qcow2", ".ova", ".ovf", ".wasm", ".swf", ".xap", ".xbap", ".air", ".jnlp", ".desktop", ".service", ".target", ".timer", ".socket", ".ko", ".kext", ".efi", ".efi32", ".efi64", ".pe", ".pdb", ".ilk", ".manifest", ".mun", ".ocx", ".tlb", ".tsp", ".ime", ".imep", ".acm", ".ax", ".mod", ".so.1", ".so.2", ".so.3"],
    "3D Models": [".obj", ".fbx", ".stl", ".gltf", ".glb", ".blend", ".dae", ".3ds", ".max", ".ma", ".mb", ".abc", ".usd", ".usda", ".usdc", ".usdz", ".ply", ".off", ".3mf", ".amf", ".wrl", ".vrml", ".x3d", ".3dm", ".step", ".stp", ".iges", ".igs", ".sat", ".sab", ".ipt", ".iam", ".idw", ".sldprt", ".sldasm", ".slddrw", ".prt", ".asm", ".f3d", ".f3z", ".skp", ".dae", ".ifc", ".ifczip", ".ifcxml", ".rvt", ".rfa", ".rte", ".rft", ".dwg", ".dxf", ".3dxml", ".jt", ".gcode", ".3dp", ".lwo", ".lws", ".c4d", ".vob", ".vwx", ".wings", ".wings3d", ".x", ".mesh", ".msh", ".m3d", ".md2", ".md3", ".md5mesh", ".md5anim", ".iqm", ".smd", ".vta", ".mdl", ".vmdl", ".vmesh", ".vmat", ".vpk", ".pak", ".unity", ".asset", ".prefab", ".uasset", ".umap", ".udatasmith", ".udm", ".gltf", ".glb", ".vrm", ".vroid", ".bvh", ".fbx", ".motion", ".mot", ".anim", ".abc", ".usd", ".usdz", ".vdb", ".svx", ".sdf", ".vol", ".nrrd", ".nii", ".nii.gz", ".mha", ".mhd", ".3ds", ".ac", ".ase", ".b3d", ".cob", ".dxf", ".enff", ".hmp", ".irr", ".lwo", ".lws", ".ms3d", ".ndo", ".nff", ".off", ".raw", ".scn", ".sib", ".ter", ".xgl", ".zgl"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".gzip", ".bz", ".bz2", ".bzip2", ".xz", ".lz", ".lzma", ".lzo", ".lz4", ".zst", ".zstd", ".br", ".brotli", ".cab", ".arj", ".ace", ".alz", ".arc", ".ark", ".a", ".pak", ".jar", ".war", ".ear", ".apk", ".ipa", ".xpi", ".crx", ".vsix", ".nupkg", ".snupkg", ".whl", ".egg", ".deb", ".rpm", ".dmg", ".iso", ".img", ".udf", ".vhd", ".vhdx", ".vmdk", ".vdi", ".qcow", ".qcow2", ".ova", ".ovf", ".z", ".taz", ".tgz", ".tbz", ".tbz2", ".tlz", ".txz", ".tzst", ".tz", ".tar.gz", ".tar.bz2", ".tar.xz", ".tar.zst", ".tar.lz", ".tar.lzma", ".tar.lzo", ".tar.lz4", ".tar.br", ".tar.Z", ".tar.z", ".cpio", ".pax", ".shar", ".sh", ".dump", ".dmp", ".wim", ".esd", ".swm", ".squashfs", ".sfs", ".appx", ".appxbundle", ".msix", ".msixbundle", ".asar", ".car", ".hfs", ".hfsx", ".xar", ".sit", ".sitx", ".sea", ".hqx", ".bin", ".uue", ".uu", ".xx", ".yenc", ".par", ".par2", ".rev", ".001", ".002", ".003", ".r00", ".r01", ".r02", ".z01", ".z02", ".z03", ".part1", ".part2", ".part3", ".7z.001", ".zip.001", ".rar.001", ".ace", ".cfs", ".dar", ".dgc", ".gca", ".ha", ".hki", ".ice", ".kgb", ".lzh", ".lha", ".lzx", ".paq6", ".paq7", ".paq8", ".pim", ".piz", ".rz", ".sda", ".sfx", ".shk", ".tar.lz4", ".uc", ".uc0", ".uc1", ".uc2", ".ucn", ".ur2", ".ue2", ".uca", ".warc", ".wacz", ".zpaq"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".woff1", ".eot", ".fon", ".fnt", ".bdf", ".pcf", ".snf", ".pfa", ".pfb", ".afm", ".pfm", ".cff", ".cid", ".otc", ".ttc", ".dfont", ".suit", ".suitcase", ".nfnt", ".lwfn", ".sfnt", ".sfd", ".ufo", ".designspace", ".vfb", ".vfc", ".vfbx", ".glyphs", ".glyphspackage", ".sfp", ".sfpng", ".amfm", ".acfm", ".inf", ".mcf", ".cha", ".chr", ".compositefont", ".fon", ".fnt", ".gdr", ".gxf", ".mf", ".mfm", ".pmt", ".sbit", ".t65", ".tfm", ".vpl", ".vfu", ".vfb", ".xfn", ".xft"],
    "Design CAD": [".dwg", ".dxf", ".dwt", ".dws", ".dgn", ".dxb", ".dxf", ".dwf", ".dwfx", ".dwl", ".dwl2", ".step", ".stp", ".iges", ".igs", ".sat", ".sab", ".3dm", ".3ds", ".sldprt", ".sldasm", ".slddrw", ".sldlfp", ".sldmat", ".sldxml", ".ipt", ".iam", ".idw", ".ipn", ".f3d", ".f3z", ".fusiondesign", ".skp", ".skb", ".layout", ".rvt", ".rfa", ".rte", ".rft", ".rva", ".ifc", ".ifczip", ".ifcxml", ".ifcjson", ".pln", ".pla", ".mod", ".gsm", ".vwx", ".mcd", ".shapr", ".shaprpart", ".shaprassembly", ".prt", ".asm", ".par", ".psm", ".sldasm", ".catpart", ".catproduct", ".catdrawing", ".3dxml", ".jt", ".x_t", ".x_b", ".3mf", ".stl", ".obj", ".fbx", ".gltf", ".glb", ".dae", ".blend", ".max", ".ma", ".mb", ".c4d", ".aep", ".ai", ".eps", ".ps", ".svg", ".svgz", ".pdf", ".indd", ".idml", ".psd", ".psb", ".xcf", ".afdesign", ".afphoto", ".afpub", ".cdr", ".cmx", ".sketch", ".fig", ".xd", ".ase", ".aseprite", ".procreate", ".kra", ".ora", ".xcf", ".clip", ".sai", ".sai2", ".afdesign", ".afphoto", ".afpub", ".dcm", ".dcd", ".dft", ".dmt", ".drw", ".prt", ".asm", ".neu", ".x_b", ".x_t", ".3d", ".3dxml", ".acis", ".amf", ".brep", ".cgr", ".ckd", ".co", ".dae", ".easm", ".edrw", ".eprt", ".f3d", ".g", ".gcode", ".gbr", ".ger", ".grb", ".idml", ".iges", ".ipt", ".mf1", ".mf2", ".mf3", ".model", ".nwc", ".nwd", ".nwf", ".par", ".pln", ".prt", ".rfa", ".rvt", ".sab", ".sat", ".sldprt", ".sldasm", ".slddrw", ".step", ".stp", ".stl", ".u3d", ".unv", ".vda", ".wrl", ".x3d", ".xgl", ".zgl"],
    "Databases": [".db", ".db3", ".sqlite", ".sqlite3", ".sqlite2", ".s3db", ".sl3", ".sql", ".sql.gz", ".sql.zip", ".dump", ".backup", ".bak", ".bkp", ".mdb", ".accdb", ".accde", ".accdr", ".accdt", ".mde", ".mdw", ".ldb", ".laccdb", ".dbf", ".ndx", ".mdx", ".cdx", ".fpt", ".dbt", ".dt", ".ib", ".ibd", ".ibdata", ".ibd2", ".frm", ".myd", ".myi", ".sdi", ".ibbackup", ".sqlitedb", ".realm", ".rdb", ".aof", ".bson", ".wt", ".sst", ".ldb", ".log", ".mdb", ".gdb", ".fdb", ".fbk", ".pdb", ".p12", ".db2", ".db2inst", ".ibm", ".oradata", ".dmp", ".exp", ".dat", ".db", ".dbf", ".ctl", ".ora", ".arc", ".arch", ".bkp", ".rman", ".mdf", ".ndf", ".ldf", ".bak", ".trn", ".xel", ".bacpac", ".dacpac", ".sdf", ".mdf", ".sqlite", ".sqlite3", ".h2.db", ".mv.db", ".trace.db", ".derby", ".db", ".log", ".wal", ".shm", ".journal", ".parquet", ".orc", ".avro", ".arrow", ".feather", ".h5", ".hdf5", ".hdf", ".nc", ".mat", ".rdata", ".rds", ".rda", ".sav", ".sas7bdat", ".sas7bcat", ".dta", ".por", ".zsav", ".xlsx", ".xls", ".csv", ".tsv", ".xml", ".json", ".jsonl", ".ndjson", ".yaml", ".yml", ".bson", ".cql", ".cqlshrc", ".cypher", ".graphml", ".gexf", ".gml", ".nt", ".nq", ".ttl", ".trig", ".trix", ".rdf", ".owl", ".db3", ".db4", ".db5", ".db6", ".kdb", ".kdbx", ".pouch", ".couch", ".nosql", ".vdi", ".vhd", ".vhdx", ".vmdk"]
}

def organize(dir=None):

    parser = argparse.ArgumentParser(prog='python_file_organizer')
    parser.add_argument('directory')

    args = parser.parse_args()

    dir = args.directory

    if os.path.isdir(dir): 
        list = os.listdir(dir) 

        length = len(list) 
    
        for x in range(length): 
            
            split = os.path.splitext(list[x])
            file_extension = split[1]

            if file_extension in file_extensions["Pictures"]:

                name = "Pictures"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])
            
            elif file_extension in file_extensions["Videos"]:

                name = "Videos"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])
            
            elif file_extension in file_extensions["Documents"]:

                name = "Documents"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])
            
            elif file_extension in file_extensions["Music"]:

                name = "Music"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

            elif file_extension in file_extensions["Scripts"]:

                name = "Scripts"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

            elif file_extension in file_extensions["Executables"]:

                name = "Executables"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

            elif file_extension in file_extensions["Archives"]:

                name = "Archives"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

            elif file_extension in file_extensions["3D Models"]:

                name = "3D Models"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])
            
            elif file_extension in file_extensions["Fonts"]:

                name = "Fonts"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])
            
            elif file_extension in file_extensions["Design CAD"]:

                name = "Design CAD"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

            elif file_extension in file_extensions["Databases"]:

                name = "Databases"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

            elif os.path.isdir(f"{dir}/{list[x]}"):
                continue

            else:
                name = "Others"
                create_folder(dir, name)
                os.replace(f"{dir}/" + list[x], f"{dir}/{name}/" + list[x])

    else:
        print("Invalid directory.")

def create_folder(dir, name):
    
    try:
        os.mkdir(f'{dir}/{name}')
    except:
        return
