# hello :)
print("A tool made by Kleopy!")
print("Build: 1\n")

import os

mapName = str(input("mapName?: "))
try:
    coachNumber = int(input("Coach Count? (1-4): "))
except:
    print("Use only numbers!")
    exit()
output = (os.getcwd() + "\\output\\" + mapName + "\\")

try:
    # Create directories
    audioFolder = (output + "Audio\\")
    os.makedirs(audioFolder, exist_ok=True)
    autodanceFolder = (output + "Autodance\\")
    os.makedirs(autodanceFolder, exist_ok=True)
    cinematicsFolder = (output + "Cinematics\\")
    os.makedirs( cinematicsFolder, exist_ok=True)
    graphFolder = (output + "Graph\\")
    os.makedirs(graphFolder, exist_ok=True)
    menuartFolder = (output + "MenuArt\\")
    os.makedirs(menuartFolder, exist_ok=True)
    menuartActorsFolder = (output + "MenuArt\\Actors\\")
    os.makedirs(menuartActorsFolder, exist_ok=True)
    menuartTexturesFolder = (output + "MenuArt\\Textures\\")
    os.makedirs(menuartTexturesFolder, exist_ok=True)
    timelineFolder = (output + "Timeline\\")
    os.makedirs(timelineFolder, exist_ok=True)
    timelineMovesFolder = (output + "Timeline\\Moves\\")
    os.makedirs(timelineMovesFolder, exist_ok=True)
    durangoMovesFolder = (timelineMovesFolder + "DURANGO\\")
    os.makedirs(durangoMovesFolder, exist_ok=True)
    orbisMovesFolder = (timelineMovesFolder + "ORBIS\\")
    os.makedirs(orbisMovesFolder, exist_ok=True)
    ps3MovesFolder = (timelineMovesFolder + "PS3\\")
    os.makedirs(ps3MovesFolder, exist_ok=True)
    wiiMovesFolder = (timelineMovesFolder + "WII\\")
    os.makedirs(wiiMovesFolder, exist_ok=True)
    wiiuMovesFolder = (timelineMovesFolder + "WIIU\\")
    os.makedirs(wiiuMovesFolder, exist_ok=True)
    x360MovesFolder = (timelineMovesFolder + "X360\\")
    os.makedirs(x360MovesFolder, exist_ok=True)
    timelinePictosFolder = (output + "Timeline\\Pictos\\")
    os.makedirs(timelinePictosFolder, exist_ok=True)
    timelineRecordingFolder = (output + "Timeline\\Recording\\")
    os.makedirs(timelineRecordingFolder, exist_ok=True)
    timelineSnippingFolder = (output + "Timeline\\Snipping\\")
    os.makedirs(timelineSnippingFolder, exist_ok=True)
    videoscoachFolder = (output + "VideosCoach\\")
    os.makedirs(videoscoachFolder, exist_ok=True)
    print("\nCreating all directories..", "DONE")

    # Root files
    iscMainScene = open(output + mapName + "_MAIN_SCENE.isc", "w", encoding="utf-8")
    iscMainScene.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="81615" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<PLATFORM_FILTER>
			<TargetFilterList platform="WII">
				<objects VAL="{mapName}_AUTODANCE"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_AUDIO" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/audio/{mapName}_audio.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="2"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_CINE" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/cinematics/{mapName}_cine.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="2"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_GRAPH" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/graph/{mapName}_graph.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="2"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_TML" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/timeline/{mapName}_tml.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="2"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_VIDEO" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/videoscoach/{mapName}_video.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="2"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName} : Template Artist - Template Title&#10;JDVer = 5, ID = 4130970130, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/songdesc.act" LUA="World/MAPS/{mapName}/songdesc.tpl">
				<COMPONENTS NAME="JD_SongDescComponent">
					<JD_SongDescComponent/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_menuart" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/menuart/{mapName}_menuart.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="3"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_AUTODANCE" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="World/MAPS/{mapName}/autodance/{mapName}_autodance.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1">
				<ENUM NAME="viewType" SEL="2"/>
			</SubSceneActor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0">
				<sceneConfigs NAME="JD_MapSceneConfig">
					<JD_MapSceneConfig hud="0" cursors="0">
						<ENUM NAME="type" SEL="1"/>
						<ENUM NAME="musicscore" SEL="2"/>
					</JD_MapSceneConfig>
				</sceneConfigs>
			</SceneConfigs>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscMainScene.close()
    print(mapName + "\\" + mapName + "_MAIN_SCENE.isc", "DONE")

    actSongDesc = open(output + "SongDesc.act", "w", encoding="utf-8")
    actSongDesc.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        LUA = "World/MAPS/{mapName}/songdesc.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "JD_SongDescComponent",
                JD_SongDescComponent =
                {{
                }},
            }},
        }},
    }}
}}
''')
    actSongDesc.close()
    print(mapName + "\\" + "SongDesc.act", "DONE")

    # Audio files
    sfiConfigMusic = open(audioFolder + "ConfigMusic.sfi", "w", encoding="utf-8")
    sfiConfigMusic.write('''<root>
  <SoundConfiguration TargetName="PC" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="PS3" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="ORBIS" Format="ADPCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="X360" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="Cafe" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="WII" Format="ADPCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="Durango" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="NX" Format="OPUS" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="GGP" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="PROSPERO" Format="PCM" IsStreamed="1" IsMusic="1"/>
  <SoundConfiguration TargetName="SCARLETT" Format="PCM" IsStreamed="1" IsMusic="1"/>
</root>''')
    sfiConfigMusic.close()
    print(mapName + "\\Audio\\" + "ConfigMusic.sfi", "DONE")

    iscAudio = open(audioFolder + mapName + "_AUDIO.isc", "w", encoding="utf-8")
    iscAudio.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="55299" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="World/MAPS/{mapName}/audio/{mapName}_musictrack.tpl">
				<COMPONENTS NAME="MusicTrackComponent">
					<MusicTrackComponent/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_sequence" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="World/MAPS/{mapName}/audio/{mapName}_sequence.tpl">
				<COMPONENTS NAME="TapeCase_Component">
					<TapeCase_Component/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscAudio.close()
    print(mapName + "\\Audio\\" + mapName + "_AUDIO.isc", "DONE")

    tplMusicTrack = open(audioFolder + mapName + "_MusicTrack.tpl", "w", encoding="utf-8")
    tplMusicTrack.write(f'''includeReference("World/MAPS/{mapName}/audio/{mapName}.trk")

params =
{{
	NAME = "Actor_Template",
	Actor_Template =
	{{
		COMPONENTS = 
		{{
			{{
				NAME="MusicTrackComponent_Template",
				MusicTrackComponent_Template =
				{{
					trackData = {{
						MusicTrackData = {{
						path = "World/MAPS/{mapName}/audio/{mapName}.wav",
                        url = "jmcs://jd-contents/{mapName}/{mapName}.ogg",
						structure = structure
						}}
					}}
				}}
			}},
		}}
	}}
}}
''')
    tplMusicTrack.close()
    print(mapName + "\\Audio\\" + mapName + "_MusicTrack.tpl", "DONE")

    tplSequence = open(audioFolder + mapName + "_Sequence.tpl", "w", encoding="utf-8")
    tplSequence.write(f'''params =
{{
	NAME = "Actor_Template",
	Actor_Template =
	{{
		COMPONENTS = 
		{{
			{{
				NAME = "TapeCase_Template", 
                TapeCase_Template = 
                {{
                    TapesRack =
                    {{
                        {{
                            TapeGroup =
                            {{
                                Entries =
                                {{
                                    {{
                                        TapeEntry =
                                        {{
                                            Label = "TML_Sequence",
                                            Path = "World/MAPS/{mapName}/audio/{mapName}.stape",
                                        }},
                                    }},
                                }},
                            }},
                        }},
                     }},
                }},
			}},
		}}
	}}
}}
''')
    tplSequence.close()
    print(mapName + "\\Audio\\" + mapName + "_Sequence.tpl", "DONE")

    # Autodance files
    actAutodance = open(autodanceFolder + mapName + "_Autodance.act", "w", encoding="utf-8")
    actAutodance.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        LUA = "World/MAPS/{mapName}/autodance/{mapName}_Autodance.tpl",
	}}
}}''')
    actAutodance.close()
    print(mapName + "\\Autodance\\" + mapName + "_Autodance.act", "DONE")

    iscAutodance = open(autodanceFolder + mapName + "_AUTODANCE.isc", "w", encoding="utf-8")
    iscAutodance.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="81615" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_autodance" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/autodance/{mapName}_autodance.act" LUA="World/MAPS/{mapName}/autodance/{mapName}_autodance.tpl">
				<COMPONENTS NAME="JD_AutodanceComponent">
					<JD_AutodanceComponent/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscAutodance.close()
    print(mapName + "\\Autodance\\" + mapName + "_AUTODANCE.isc", "DONE")

    tplAutodance = open(autodanceFolder + mapName + "_Autodance.tpl", "w", encoding="utf-8")
    tplAutodance.write(f'''includeReference("World/MAPS/{mapName}/autodance/{mapName}.adrecording")
includeReference("World/MAPS/{mapName}/autodance/{mapName}.advideo")

params =
{{
	NAME = "Actor_Template",
	Actor_Template =
	{{
		COMPONENTS = 
		{{
			{{
				NAME="JD_AutodanceComponent_Template",
				JD_AutodanceComponent_Template =
				{{
					song = "{mapName}",
					autodanceData =
					{{
						JD_AutodanceData = 
						{{
							recording_structure = autodance_recording_structure,
							video_structure = autodance_video_structure,
							autodanceSoundPath = "World/MAPS/{mapName}/autodance/{mapName}.ogg"
						}}
					}}
				}}
			}},
		}}
	}}
}}
''')
    tplAutodance.close()
    print(mapName + "\\Autodance\\" + mapName + "_Autodance.tpl", "DONE")

    # Cinematics files
    iscCine = open(cinematicsFolder + mapName + "_CINE.isc", "w", encoding="utf-8")
    iscCine.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="55299" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_MainSequence" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/cinematics/{mapName}_mainsequence.act" LUA="World/MAPS/{mapName}/cinematics/{mapName}_mainsequence.tpl">
				<COMPONENTS NAME="MasterTape">
					<MasterTape bankState="4294967295" />
				</COMPONENTS>
			</Actor>
		</ACTORS>		
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0" />
		</sceneConfigs>
	</Scene>
</root>
''')
    iscCine.close()
    print(mapName + "\\Cinematics\\" + mapName + "_CINE.isc", "DONE")

    actMainSequence = open(cinematicsFolder + mapName + "_MainSequence.act", "w", encoding="utf-8")
    actMainSequence.write(f'''params = 
{{
    NAME = "Actor", 
    Actor = 
    {{
        LUA = "World/MAPS/{mapName}/cinematics/{mapName}_mainsequence.tpl", 
        COMPONENTS = 
        {{
            
            {{
                NAME = "MasterTape"
            }}
        }}
    }}
}}''')
    actMainSequence.close()
    print(mapName + "\\Cinematics\\" + mapName + "_MainSequence.act", "DONE")

    tplMainSequence = open(cinematicsFolder + mapName + "_MainSequence.tpl", "w", encoding="utf-8")
    tplMainSequence.write(f'''params = 
{{
    NAME = "Actor_Template", 
    Actor_Template = 
    {{
        COMPONENTS = 
        {{
            
            {{
                NAME = "MasterTape_Template", 
                MasterTape_Template = 
                {{
                    TapePath = "World/MAPS/{mapName}/Cinematics/{mapName}_MainSequence.tape"
                }}
            }}
        }}
    }}
}}''')
    tplMainSequence.close()
    print(mapName + "\\Cinematics\\" + mapName + "_MainSequence.tpl", "DONE")

    # Graph file (only the default one)
    iscGraph = open(graphFolder + mapName + "_GRAPH.isc", "w", encoding="utf-8")
    iscGraph.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="55299" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="10.0" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" POS2D="0.0 0.0" ANGLE="0.0" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl"/>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscGraph.close()
    print(mapName + "\\Graph\\" + mapName + "_GRAPH.isc", "DONE")

    #MenuArt files
    iscMenuArt = open(menuartFolder + mapName + "_MENUART.isc", "w", encoding="utf-8")
    iscMenuArtContent = ""
    if coachNumber == 1:
        iscMenuArtContent = (f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="140999" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
		<PLATFORM_FILTER>
			<TargetFilterList platform="WII">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="PS3">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="X360">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="WIIU">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="ORBIS">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="DURANGO">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online_Kids" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online_Kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online_Kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumcoach" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumcoach.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumbkg" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumbkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_banner_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_1" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_1.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_map_bkg" DEFAULTENABLE="1" POS2D="1487.410034 350.000000" ANGLE="0.000000" INSTANCEDATAFILE="world/maps/{mapName}/menuart/actors/{mapName}_map_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="world/maps/{mapName}/menuart/textures/{mapName}_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
								<outlinedMaskParams>
									<OutlinedMaskMaterialParams maskColor="0.000000 0.000000 0.000000 0.000000" outlineColor="0.000000 0.000000 0.000000 0.000000" thickness="1.000000"/>
								</outlinedMaskParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    elif coachNumber == 2:
        iscMenuArtContent = (f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="140999" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
		<PLATFORM_FILTER>
			<TargetFilterList platform="WII">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="PS3">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="X360">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="WIIU">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="ORBIS">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="DURANGO">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online_Kids" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online_Kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online_Kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumcoach" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumcoach.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumbkg" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumbkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_banner_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_1" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_1.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_2" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_2.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_map_bkg" DEFAULTENABLE="1" POS2D="1487.410034 350.000000" ANGLE="0.000000" INSTANCEDATAFILE="world/maps/{mapName}/menuart/actors/{mapName}_map_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="world/maps/{mapName}/menuart/textures/{mapName}_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
								<outlinedMaskParams>
									<OutlinedMaskMaterialParams maskColor="0.000000 0.000000 0.000000 0.000000" outlineColor="0.000000 0.000000 0.000000 0.000000" thickness="1.000000"/>
								</outlinedMaskParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    elif coachNumber == 3:
        iscMenuArtContent = (f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="140999" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
		<PLATFORM_FILTER>
			<TargetFilterList platform="WII">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="PS3">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="X360">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="WIIU">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="ORBIS">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="DURANGO">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online_Kids" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online_Kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online_Kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumcoach" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumcoach.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumbkg" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumbkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_banner_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_1" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_1.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_2" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_2.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_3" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_3.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_map_bkg" DEFAULTENABLE="1" POS2D="1487.410034 350.000000" ANGLE="0.000000" INSTANCEDATAFILE="world/maps/{mapName}/menuart/actors/{mapName}_map_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="world/maps/{mapName}/menuart/textures/{mapName}_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
								<outlinedMaskParams>
									<OutlinedMaskMaterialParams maskColor="0.000000 0.000000 0.000000 0.000000" outlineColor="0.000000 0.000000 0.000000 0.000000" thickness="1.000000"/>
								</outlinedMaskParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    elif coachNumber == 4:
        iscMenuArtContent = (f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="140999" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
		<PLATFORM_FILTER>
			<TargetFilterList platform="WII">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="PS3">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="X360">
				<objects VAL="{mapName}_banner_bkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="WIIU">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="ORBIS">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<PLATFORM_FILTER>
			<TargetFilterList platform="DURANGO">
				<objects VAL="{mapName}_cover_generic"/>
				<objects VAL="{mapName}_cover_albumbkg"/>
			</TargetFilterList>
		</PLATFORM_FILTER>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online_Kids" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online_Kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online_Kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_online" POS2D="-150.00000 0.00000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_online.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumcoach" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumcoach.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_albumbkg" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_albumbkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_banner_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_1" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_1.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_2" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_2.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_3" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_3.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="{mapName}_coach_4" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_coach_4.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="6"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="World/_COMMON/MatShader/MultiTexture_1Layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_coach_4.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="6"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_map_bkg" DEFAULTENABLE="1" POS2D="1487.410034 350.000000" ANGLE="0.000000" INSTANCEDATAFILE="world/maps/{mapName}/menuart/actors/{mapName}_map_bkg.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
				<COMPONENTS NAME="MaterialGraphicComponent">
					<MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="world/maps/{mapName}/menuart/textures/{mapName}_map_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
								<outlinedMaskParams>
									<OutlinedMaskMaterialParams maskColor="0.000000 0.000000 0.000000 0.000000" outlineColor="0.000000 0.000000 0.000000 0.000000" thickness="1.000000"/>
								</outlinedMaskParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</MaterialGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscMenuArt.write(iscMenuArtContent)
    iscMenuArt.close()
    print(mapName + "\\MenuArt\\" + mapName + "_MENUART.isc", "DONE")

    #MenuArt Actors files
    actBannerBkg = open(menuartActorsFolder + mapName + "_banner_bkg.act", "w", encoding="utf-8")
    actBannerBkg.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0,00000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_banner_bkg.tga",

                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actBannerBkg.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_banner_bkg.act", "DONE")

    ignoreCoach = open(menuartActorsFolder + mapName + "_Coach.ignore", "w", encoding="utf-8")
    ignoreCoach.write('''${if eq(NumberCoach, 1):
${MapName}$_Coach_2.act
${MapName}$_Coach_3.act
${MapName}$_Coach_4.act
}$

${if eq(NumberCoach, 2):
${MapName}$_Coach_3.act
${MapName}$_Coach_4.act
}$

${if eq(NumberCoach, 3):
${MapName}$_Coach_4.act
}$
''')
    ignoreCoach.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Coach.ignore", "DONE")

    actCoach1 = open(menuartActorsFolder + mapName + "_Coach_1.act", "w", encoding="utf-8")
    actCoach1.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0.000000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    anchor = 6,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_coach_1.tga",
                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actCoach1.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Coach_1.act", "DONE")

    if coachNumber > 1:
        actCoach2 = open(menuartActorsFolder + mapName + "_Coach_2.act", "w", encoding="utf-8")
        actCoach2.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0.000000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    anchor = 6,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_coach_2.tga",
                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
        actCoach2.close()
        print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Coach_2.act", "DONE")

    if coachNumber > 2:
        actCoach3 = open(menuartActorsFolder + mapName + "_Coach_3.act", "w", encoding="utf-8")
        actCoach3.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0.000000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    anchor = 6,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_coach_3.tga",
                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
        actCoach3.close()
        print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Coach_3.act", "DONE")

    if coachNumber > 3:
        actCoach4 = open(menuartActorsFolder + mapName + "_Coach_4.act", "w", encoding="utf-8")
        actCoach4.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0.000000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    anchor = 6,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_coach_4.tga",
                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
        actCoach4.close()
        print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Coach_4.act", "DONE")

    actCoverAlbumBkg = open(menuartActorsFolder + mapName + "_Cover_AlbumBkg.act", "w", encoding="utf-8")
    actCoverAlbumBkg.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0,00000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumbkg.tga",

                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actCoverAlbumBkg.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Cover_AlbumBkg.act", "DONE")

    actCoverAlbumCoach = open(menuartActorsFolder + mapName + "_Cover_AlbumCoach.act", "w", encoding="utf-8")
    actCoverAlbumCoach.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0.000000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    anchor = 6,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_cover_albumcoach.tga",
                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actCoverAlbumCoach.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Cover_AlbumCoach.act", "DONE")

    actCoverGeneric = open(menuartActorsFolder + mapName + "_Cover_Generic.act", "w", encoding="utf-8")
    actCoverGeneric.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0,00000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic.tga",

                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actCoverGeneric.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Cover_Generic.act", "DONE")

    actCoverOnline = open(menuartActorsFolder + mapName + "_Cover_Online.act", "w", encoding="utf-8")
    actCoverOnline.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online.tga",

                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actCoverOnline.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Cover_Online.act", "DONE")

    actCoverOnlineKids = open(menuartActorsFolder + mapName + "_Cover_Online_Kids.act", "w", encoding="utf-8")
    actCoverOnlineKids.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_cover_online_Kids.tga",

                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actCoverOnlineKids.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_Cover_Online_Kids.act", "DONE")

    actMapBkg = open(menuartActorsFolder + mapName + "_map_bkg.act", "w", encoding="utf-8")
    actMapBkg.write(f'''params =
{{
    NAME="Actor",
    Actor =
    {{
        RELATIVEZ = 0,00000,
        LUA = "enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl",
        COMPONENTS =
        {{
            {{
                NAME = "MaterialGraphicComponent",
                MaterialGraphicComponent =
                {{
                    disableLight = 0,
                    material =
                    {{
                        GFXMaterialSerializable =
                        {{
                            textureSet =
                            {{
                                GFXMaterialTexturePathSet =
                                {{
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_map_bkg.tga",

                                }},
                            }},
                            shaderPath = "World/_COMMON/MatShader/MultiTexture_1Layer.msh",
                        }},
                    }},
                }},
            }},
        }},
    }}
}}
''')
    actMapBkg.close()
    print(mapName + "\\MenuArt\\Actors\\" + mapName + "_map_bkg.act", "DONE")

    #Timeline files
    iscTml = open(timelineFolder + mapName + "_TML.isc", "w", encoding="utf-8")
    iscTml.write(f'''<?xml version="1.0" encoding="iso-8859-1"?>
<root>
	<Scene ENGINE_VERSION="64087" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_tml_dance" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/Timeline/{mapName}_TML_Dance.act" LUA="World/MAPS/{mapName}/Timeline/{mapName}_TML_Dance.tpl">
				<COMPONENTS NAME="TapeCase_Component">
					<TapeCase_Component/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{mapName}_tml_karaoke" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/Timeline/{mapName}_TML_Karaoke.act" LUA="World/MAPS/{mapName}/Timeline/{mapName}_TML_Karaoke.tpl">
				<COMPONENTS NAME="TapeCase_Component">
					<TapeCase_Component/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
	</Scene>
</root>''')
    iscTml.close()
    print(mapName + "\\Timeline\\" + mapName + "_TML.isc", "DONE")

    actTmlDance = open(timelineFolder + mapName + "_TML_Dance.act", "w", encoding="utf-8")
    actTmlDance.write(f'''params = 
{{
    NAME = "Actor", 
    Actor = 
    {{
        LUA = "World/MAPS/{mapName}/Timeline/{mapName}_TML_Dance.tpl", 
        COMPONENTS = 
        {{            
            {{
                NAME = "TapeCase_Component",
            }}
        }}
    }}
}}
''')
    actTmlDance.close()
    print(mapName + "\\Timeline\\" + mapName + "_TML_Dance.act", "DONE")

    tplTmlDance = open(timelineFolder + mapName + "_TML_Dance.tpl", "w", encoding="utf-8")
    tplTmlDance.write(f'''params = 
{{
    NAME = "Actor_Template", 
    Actor_Template = 
    {{
        COMPONENTS = 
        {{
            
            {{
                NAME = "TapeCase_Template", 
                TapeCase_Template = 
                {{
                    TapesRack =
                    {{
                        {{
                            TapeGroup =
                            {{
                                Entries =
                                {{
                                    {{
                                        TapeEntry =
                                        {{
                                            Label = "TML_Motion",
                                            Path = "World/MAPS/{mapName}/Timeline/{mapName}_TML_Dance.dtape",
                                        }},
                                    }},
                                }},
                            }},
                        }},
                     }},
                }},
            }}
        }}
    }}
}}
''')
    tplTmlDance.close()
    print(mapName + "\\Timeline\\" + mapName + "_TML_Dance.tpl", "DONE")

    actTmlKaraoke = open(timelineFolder + mapName + "_TML_Karaoke.act", "w", encoding="utf-8")
    actTmlKaraoke.write(f'''params = 
{{
    NAME = "Actor", 
    Actor = 
    {{
        LUA = "World/MAPS/{mapName}/Timeline/{mapName}_TML_Karaoke.tpl", 
        COMPONENTS = 
        {{            
            {{
                NAME = "TapeCase_Component",
            }}
        }}
    }}
}}
''')
    actTmlKaraoke.close()
    print(mapName + "\\Timeline\\" + mapName + "_TML_Karaoke.act", "DONE")

    tplTmlKaraoke = open(timelineFolder + mapName + "_TML_Karaoke.tpl", "w", encoding="utf-8")
    tplTmlKaraoke.write(f'''params = 
{{
    NAME = "Actor_Template", 
    Actor_Template = 
    {{
        COMPONENTS = 
        {{
            
            {{
                NAME = "TapeCase_Template", 
                TapeCase_Template = 
                {{
                    TapesRack =
                    {{
                        {{
                            TapeGroup =
                            {{
                                Entries =
                                {{
                                    {{
                                        TapeEntry =
                                        {{
                                            Label = "TML_Karaoke",
                                            Path = "World/MAPS/{mapName}/Timeline/{mapName}_TML_Karaoke.ktape",
                                        }},
                                    }},
                                }},
                            }},
                        }},
                     }},
                }},
            }}
        }}
    }}
}}
''')
    tplTmlKaraoke.close()
    print(mapName + "\\Timeline\\" + mapName + "_TML_Karaoke.tpl", "DONE")

    #VideosCoach files
    iscVideo = open(videoscoachFolder + mapName + "_VIDEO.isc", "w", encoding="utf-8")
    iscVideo.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="55299" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/videoscoach/video_player_main.act" LUA="world/_common/videoscreen/video_player_main.tpl">
			</Actor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="world/_common/videoscreen/video_output_main.act" LUA="world/_common/videoscreen/video_output_main.tpl">
				<COMPONENTS NAME="PleoTextureGraphicComponent">
					<PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="-1" customAnchor="0.000000 0.000000" spriteIndex="4294967295" Orientation="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
						<PrimitiveParameters>
							<GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000" FrontLightBrightness="0.000000" FrontLightContrast="1.000000" BackLightBrightness="0.000000" BackLightContrast="1.000000" colorFog="0.000000 0.000000 0.000000 0.000000" DynamicFogFactor="1.000000" useStaticFog="0" RenderInReflections="1">
								<ENUM NAME="gfxOccludeInfo" SEL="0"/>
							</GFXPrimitiveParam>
						</PrimitiveParameters>
						<ENUM NAME="anchor" SEL="1"/>
						<material>
							<GFXMaterialSerializable ATL_Channel="0" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
								<textureSet>
									<GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
								</textureSet>
								<materialParams>
									<GFXMaterialSerializableParam Reflector_factor="0.000000"/>
								</materialParams>
							</GFXMaterialSerializable>
						</material>
						<ENUM NAME="oldAnchor" SEL="1"/>
					</PleoTextureGraphicComponent>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscVideo.close()
    print(mapName + "\\VideosCoach\\" + mapName + "_VIDEO.isc", "DONE")

    iscVideoMapPreview = open(videoscoachFolder + mapName + "_VIDEO_MAP_PREVIEW.isc", "w", encoding="utf-8")
    iscVideoMapPreview.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="55299" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/videoscoach/video_player_map_preview.act" LUA="world/_common/videoscreen/video_player_map_preview.tpl">
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0"/>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscVideoMapPreview.close()
    print(mapName + "\\VideosCoach\\" + mapName + "_VIDEO_MAP_PREVIEW.isc", "DONE")

    actVideoPlayerMain = open(videoscoachFolder + "video_player_main.act", "w", encoding="utf-8")
    actVideoPlayerMain.write(f'''params =
{{
    NAME="Actor",
    Actor = 
    {{
        LUA = "world/_common/videoscreen/video_player_main.tpl",
        COMPONENTS =
        {{
            {{
                NAME="PleoComponent",
                PleoComponent = 
                {{
                    Video = "World/MAPS/{mapName}/videoscoach/{mapName}.webm",
					dashMPD = "World/MAPS/{mapName}/videoscoach/{mapName}.mpd",
                }},
            }},
        }},
    }},
}}
''')
    actVideoPlayerMain.close()
    print(mapName + "\\VideosCoach\\" + "video_player_main.act", "DONE")

    actVideoPlayerMapPreview = open(videoscoachFolder + "video_player_map_preview.act", "w", encoding="utf-8")
    actVideoPlayerMapPreview.write(f'''params =
{{
    NAME="Actor",
    Actor = 
    {{
        LUA = "world/_common/videoscreen/video_player_map_preview.tpl",
        COMPONENTS =
        {{
            {{
                NAME="PleoComponent",
                PleoComponent = 
                {{
                    Video = "World/MAPS/{mapName}/videoscoach/{mapName}.webm",
					dashMPD = "World/MAPS/{mapName}/videoscoach/{mapName}.mpd",
					channelID = "{mapName}",
                }},
            }},
        }},
    }},
}}
''')
    actVideoPlayerMapPreview.close()
    print(mapName + "\\VideosCoach\\" + "video_player_map_preview.act", "DONE")
except:
    print("\nThere's an error somewhere!")
