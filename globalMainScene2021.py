# hello :)
print("Welcome to the UbiArt Framework \033[34mlua MainScene\033[0m \033[1mmaker\033[0m!")
print("(It was made specifically for the \033[1mJD2021_TU1\033[0m build that has been publicly shared)")
print("This is a tool made by \033[4mKleopy\033[0m")
print("Code version: 6\n")

import os, shutil

mapName = str(input("mapName?: "))
try:
    coachNumber = int(input("Coach Count? (1-4): "))
except:
    print("\033[31mUse only numbers!\033[0m")
    exit()
if coachNumber > 4:
    print("\033[31mNo more than 4 players are allowed!\033[0m")
    exit()
output = (os.getcwd() + "/output/" + mapName + "/")

try:
    print("\nLog:")
    rawDataDir = "_RawData/"
    # Create directories
    audioFolder = (output + "Audio/")
    os.makedirs(audioFolder, exist_ok=True)
    autodanceFolder = (output + "Autodance/")
    os.makedirs(autodanceFolder, exist_ok=True)
    cinematicsFolder = (output + "Cinematics/")
    os.makedirs( cinematicsFolder, exist_ok=True)
    graphFolder = (output + "Graph/")
    os.makedirs(graphFolder, exist_ok=True)
    menuartFolder = (output + "MenuArt/")
    os.makedirs(menuartFolder, exist_ok=True)
    rawDataMenuArt = (menuartFolder + rawDataDir)
    os.makedirs(rawDataMenuArt, exist_ok=True)
    menuartActorsFolder = (output + "MenuArt/Actors/")
    os.makedirs(menuartActorsFolder, exist_ok=True)
    menuartTexturesFolder = (output + "MenuArt/Textures/")
    os.makedirs(menuartTexturesFolder, exist_ok=True)
    timelineFolder = (output + "Timeline/")
    os.makedirs(timelineFolder, exist_ok=True)
    timelineMovesFolder = (output + "Timeline/Moves/")
    os.makedirs(timelineMovesFolder, exist_ok=True)
    durangoMovesFolder = (timelineMovesFolder + "DURANGO/")
    os.makedirs(durangoMovesFolder, exist_ok=True)
    orbisMovesFolder = (timelineMovesFolder + "ORBIS/")
    os.makedirs(orbisMovesFolder, exist_ok=True)
    ps3MovesFolder = (timelineMovesFolder + "PS3/")
    os.makedirs(ps3MovesFolder, exist_ok=True)
    wiiMovesFolder = (timelineMovesFolder + "WII/")
    os.makedirs(wiiMovesFolder, exist_ok=True)
    wiiuMovesFolder = (timelineMovesFolder + "WIIU/")
    os.makedirs(wiiuMovesFolder, exist_ok=True)
    x360MovesFolder = (timelineMovesFolder + "X360/")
    os.makedirs(x360MovesFolder, exist_ok=True)
    timelinePictosFolder = (output + "Timeline/Pictos/")
    os.makedirs(timelinePictosFolder, exist_ok=True)
    rawDataPictos = (timelinePictosFolder + rawDataDir)
    os.makedirs(rawDataPictos, exist_ok=True)
    timelineRecordingFolder = (output + "Timeline/Recording/")
    os.makedirs(timelineRecordingFolder, exist_ok=True)
    timelineSnippingFolder = (output + "Timeline/Snipping/")
    os.makedirs(timelineSnippingFolder, exist_ok=True)
    videoscoachFolder = (output + "VideosCoach/")
    os.makedirs(videoscoachFolder, exist_ok=True)
    print("\033[32mDONE\033[0m", "Created all directory...")

    # Root/World files
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
    print("\033[32mDONE\033[0m", mapName + "/" + mapName + "_MAIN_SCENE.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/" + "SongDesc.act")

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
    print("\033[32mDONE\033[0m", mapName + "/Audio/" + "ConfigMusic.sfi")

    stape = open(audioFolder + mapName + ".stape", "w", encoding="utf-8")
    stape.write(f'''params =
{{
    NAME = "Tape",
    Tape = 
    {{
        TapeClock = 0, -- TapeClock_ConductorGameplay
        TapeBarCount = 1,
        FreeResourcesAfterPlay = 0,
        MapName = "{mapName}",
        SoundwichEvent = "",
    }},
}}
''')
    stape.close()
    print("\033[32mDONE\033[0m", mapName + "/Audio/" + mapName + ".stape")

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
    print("\033[32mDONE\033[0m", mapName + "/Audio/" + mapName + "_AUDIO.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/Audio/" + mapName + "_MusicTrack.tpl")

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
    print("\033[32mDONE\033[0m", mapName + "/Audio/" + mapName + "_Sequence.tpl")

    # Autodance files
    adrecording = open(autodanceFolder + mapName + ".adrecording", "w", encoding="utf-8")
    adrecording.write(f'''autodance_recording_structure = 
{{
    JD_AutodanceRecordingStructure = 
    {{
        records = {{  }}, 
        GameMode = 1
    }}
}}''')
    adrecording.close()
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + ".adrecording")

    adtape = open(autodanceFolder + mapName + ".adtape", "w", encoding="utf-8")
    adtape.write(f'''params =
{{
    NAME = "Tape",
    Tape = 
    {{
        Tracks =
        {{
            {{
                NAME = "MusicLoopTrack",
                MusicLoopTrack = 
                {{
                    Id = 669036043,
                    Name = "Replay Music",
                }},
            }},
            {{
                NAME = "RecordClipTrack",
                RecordClipTrack = 
                {{
                    Id = 16310479,
                    Name = "Record",
                }},
            }},
            {{
                NAME = "UsedRecordingClipTrack",
                UsedRecordingClipTrack = 
                {{
                    Id = 2821542699,
                    Name = "Used Recordings",
                }},
            }},
            {{
                NAME = "ReplayClipTrack",
                ReplayClipTrack = 
                {{
                    Id = 3198637222,
                    Name = "Replay",
                }},
            }},
        }},
        TapeClock = 2, -- TapeClock_Engine
        TapeBarCount = 1,
        FreeResourcesAfterPlay = 0,
        MapName = "{mapName}",
        SoundwichEvent = "",
    }},
}}
''')
    adtape.close()
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + ".adtape")

    advideo = open(autodanceFolder + mapName + ".advideo", "w", encoding="utf-8")
    advideo.write(f'''autodance_video_structure = 
{{
    JD_AutodanceVideoStructure = 
    {{
        GameMode = 1, 
        PropIdCounter = 0, 
        PropConfigIdCounter = 0, 
        SongStartPosition = 0.000000, 
        Duration = 32.000000, 
        FramePath = "invalid path", 
        FadeOutDuration = 3.000000, 
        AnimatedFramePath = "invalid path", 
        GroundPlanePath = "invalid path", 
        FirstLayerTripleBackgroundPath = "invalid path", 
        SecondLayerTripleBackgroundPath = "invalid path", 
        ThirdLayerTripleBackgroundPath = "invalid path", 
        ThumbnailTime = 0.000000, 
        background_effect = 
        {{
            AutoDanceFxDesc = 
            {{
                HalftoneFactor = 0.000000, 
                HalftoneCutoutLevels = 256.000000, 
                SobColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                Opacity = 1.000000, 
                LowToMid = 0.333000, 
                LowToMidWidth = 0.150000, 
                MidToHigh = 0.666000, 
                MidToHighWidth = 0.150000, 
                ColorLow = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColorMid = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColorHigh = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                UVBlackoutFactor = 0.000000, 
                UVBlackoutDesaturation = 0.200000, 
                UVBlackoutContrast = 4.000000, 
                UVBlackoutBrightness = 0.000000, 
                UVBlackoutColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.549020, 
                        y = 0.549020, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                RefractionFactor = 0.000000, 
                RefractionOpacity = 0.200000, 
                RefractionTint = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                RefractionScale = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.030000, 
                        y = 0.030000, 
                        z = 0.030000, 
                        w = 0.030000
                    }}
                }}, 
                SaturationModifier = 0.000000, 
                ColoredShivaColor0 = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColoredShivaColor1 = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColoredShivaColor2 = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColoredShivaThresholds = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.100000, 
                        y = 0.300000, 
                        z = 0.600000, 
                        w = 0.950000
                    }}
                }}, 
                OverlayBlendColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.721569, 
                        y = 0.639216, 
                        z = 0.756863, 
                        w = 1.000000
                    }}
                }}, 
                OverlayBlendFactor = 0.000000, 
                BackgroundSobelColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                BackgroundSobelFactor = 0.000000, 
                ToonFactor = 0.000000, 
                TintMulColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                TintMulColorFactor = 0.000000, 
                ScreenBlendInverseAlphaFactor = 0.000000, 
                ScreenBlendInverseAlphaScaleX = 0.000000, 
                ScreenBlendInverseAlphaScaleY = 0.000000, 
                ScreenBlendInverseAlphaTransX = 0.000000, 
                ScreenBlendInverseAlphaTransY = 0.000000, 
                FloorPlaneFactor = 0.000000, 
                FloorPlaneTiles = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 8.000000, 
                        y = 8.000000, 
                        z = 0.000000, 
                        w = 0.000000
                    }}
                }}, 
                FloorSpeedX = 0.000000, 
                FloorSpeedY = 0.000000, 
                FloorWaveSpeed = 0.000000, 
                FloorBlendMode = 0, 
                TripleLayerBackgroundFactor = 0.000000, 
                TripleLayerBackgroundTintColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 0.000000
                    }}
                }}, 
                TripleLayerBackgroundSpeedX = 0.000000, 
                TripleLayerBackgroundSpeedY = 0.000000
            }}
        }}, 
        player_effect = 
        {{
            AutoDanceFxDesc = 
            {{
                HalftoneFactor = 0.000000, 
                HalftoneCutoutLevels = 256.000000, 
                SobColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                Opacity = 1.000000, 
                LowToMid = 0.333000, 
                LowToMidWidth = 0.150000, 
                MidToHigh = 0.666000, 
                MidToHighWidth = 0.150000, 
                ColorLow = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColorMid = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColorHigh = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                UVBlackoutFactor = 0.000000, 
                UVBlackoutDesaturation = 0.200000, 
                UVBlackoutContrast = 4.000000, 
                UVBlackoutBrightness = 0.000000, 
                UVBlackoutColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.549020, 
                        y = 0.549020, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                RefractionFactor = 0.000000, 
                RefractionOpacity = 0.200000, 
                RefractionTint = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                RefractionScale = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.030000, 
                        y = 0.030000, 
                        z = 0.030000, 
                        w = 0.030000
                    }}
                }}, 
                SaturationModifier = 0.000000, 
                ColoredShivaColor0 = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColoredShivaColor1 = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColoredShivaColor2 = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                ColoredShivaThresholds = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.100000, 
                        y = 0.300000, 
                        z = 0.600000, 
                        w = 0.950000
                    }}
                }}, 
                OverlayBlendColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.721569, 
                        y = 0.639216, 
                        z = 0.756863, 
                        w = 1.000000
                    }}
                }}, 
                OverlayBlendFactor = 0.000000, 
                BackgroundSobelColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                BackgroundSobelFactor = 0.000000, 
                ToonFactor = 0.000000, 
                TintMulColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 1.000000
                    }}
                }}, 
                TintMulColorFactor = 0.000000, 
                ScreenBlendInverseAlphaFactor = 0.000000, 
                ScreenBlendInverseAlphaScaleX = 0.000000, 
                ScreenBlendInverseAlphaScaleY = 0.000000, 
                ScreenBlendInverseAlphaTransX = 0.000000, 
                ScreenBlendInverseAlphaTransY = 0.000000, 
                FloorPlaneFactor = 0.000000, 
                FloorPlaneTiles = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 8.000000, 
                        y = 8.000000, 
                        z = 0.000000, 
                        w = 0.000000
                    }}
                }}, 
                FloorSpeedX = 0.000000, 
                FloorSpeedY = 0.000000, 
                FloorWaveSpeed = 0.000000, 
                FloorBlendMode = 0, 
                TripleLayerBackgroundFactor = 0.000000, 
                TripleLayerBackgroundTintColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 0.000000, 
                        z = 0.000000, 
                        w = 0.000000
                    }}
                }}, 
                TripleLayerBackgroundSpeedX = 0.000000, 
                TripleLayerBackgroundSpeedY = 0.000000, 
                ThickMiddle = 0.400000, 
                ThickInner = 0.100000, 
                ThickSmooth = 0.100000, 
                OutColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 1.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 0.000000
                    }}
                }}, 
                ShvNbFrames = 0, 
                PartsScale = 
                {{
                    
                    {{
                        VAL = 1.000000
                    }}, 
                    
                    {{
                        VAL = 1.000000
                    }}, 
                    
                    {{
                        VAL = 1.000000
                    }}, 
                    
                    {{
                        VAL = 1.000000
                    }}, 
                    
                    {{
                        VAL = 1.000000
                    }}
                }}, 
                SlimeFactor = 0.000000, 
                SlimeAmbient = 0.200000, 
                SlimeNormalTiling = 7.000000, 
                SlimeLightAngle = 0.000000, 
                SlimeRefraction = 0.100000, 
                SlimeRefractionIndex = 1.100000, 
                SlimeSpecular = 1.100000, 
                SlimeSpecularPower = 2.000000, 
                SlimeColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.894118, 
                        y = 0.294118, 
                        z = 1.000000, 
                        w = 0.549020
                    }}
                }}, 
                ToonCutoutLevels = 256.000000, 
                PlayerGlowFactor = 0.000000, 
                PlayerGlowColor = 
                {{
                    GFX_Vector4 = 
                    {{
                        x = 0.000000, 
                        y = 1.000000, 
                        z = 1.000000, 
                        w = 1.000000
                    }}
                }}, 
                SwapHeadWithPlayer = 
                {{
                    
                    {{
                        VAL = 0
                    }}, 
                    
                    {{
                        VAL = 1
                    }}, 
                    
                    {{
                        VAL = 2
                    }}, 
                    
                    {{
                        VAL = 3
                    }}, 
                    
                    {{
                        VAL = 4
                    }}, 
                    
                    {{
                        VAL = 5
                    }}
                }}, 
                AnimatePlayerHead = 
                {{
                    
                    {{
                        VAL = 0
                    }}, 
                    
                    {{
                        VAL = 0
                    }}, 
                    
                    {{
                        VAL = 0
                    }}, 
                    
                    {{
                        VAL = 0
                    }}, 
                    
                    {{
                        VAL = 0
                    }}, 
                    
                    {{
                        VAL = 0
                    }}
                }}, 
                StartRadius = 0.000000, 
                EndRadius = 2.000000, 
                RadiusVariance = 0.000000, 
                RadiusNoiseRate = 0.000000, 
                RadiusNoiseAmp = 0.000000, 
                MinSpin = 0.000000, 
                MaxSpin = 0.000000, 
                DirAngle = 0.000000, 
                MinWanderRate = 0.000000, 
                MaxWanderRate = 0.000000, 
                MinWanderAmp = 0.000000, 
                MaxWanderAmp = 0.000000, 
                MinSpeed = 2.000000, 
                MaxSpeed = 4.000000, 
                MotionPower = 1.000000, 
                Amount = 0.000000, 
                ImageID = 0, 
                StartR = 0.000000, 
                StartG = 0.000000, 
                StartB = 0.000000, 
                EndR = 1.000000, 
                EndG = 1.000000, 
                EndB = 1.000000, 
                StartAlpha = 1.000000, 
                EndAlpha = 1.000000, 
                AnimatedHeadTotalTime = 20.000000, 
                AnimatedHeadRestTime = 16.000000, 
                AnimatedHeadFrameTime = 0.600000, 
                AnimatedHeadMaxDistance = 1.250000, 
                AnimatedHeadMaxAngle = 1.200000, 
                TexturedOutlineFactor = 0.000000, 
                TexturedOutlineTiling = 0.000000
            }}
        }}
    }}
}}''')
    advideo.close()
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + ".advideo")

    shutil.copyfile("assets/defaultAutodance.ogg", autodanceFolder + mapName + ".ogg")
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + ".ogg")

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
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + "_Autodance.act")

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
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + "_AUTODANCE.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/Autodance/" + mapName + "_Autodance.tpl")

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
    print("\033[32mDONE\033[0m", mapName + "/Cinematics/" + mapName + "_CINE.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/Cinematics/" + mapName + "_MainSequence.act")

    tapeMainSequence = open(cinematicsFolder + mapName + "_MainSequence.tape", "w", encoding="utf-8")
    tapeMainSequence.write(f'''params =
{{
    NAME = "Tape",
    Tape = 
    {{
        TapeClock = 0, -- TapeClock_ConductorGameplay
        TapeBarCount = 1,
        FreeResourcesAfterPlay = 0,
        MapName = "{mapName}",
        SoundwichEvent = "",
    }},
}}
''')
    tapeMainSequence.close()
    print("\033[32mDONE\033[0m", mapName + "/Cinematics/" + mapName + "_MainSequence.tape")

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
    print("\033[32mDONE\033[0m", mapName + "/Cinematics/" + mapName + "_MainSequence.tpl")

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
    print("\033[32mDONE\033[0m", mapName + "/Graph/" + mapName + "_GRAPH.isc")

    #MenuArt files
    iscColorHelper = open(menuartFolder + mapName + "_colorhelper.isc", "w", encoding="utf-8")
    iscColorHelper.write(f'''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
	<Scene ENGINE_VERSION="0" GRIDUNIT="1.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="_map" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/ui/screens/_map/_map.tpl">
				<COMPONENTS NAME="UIScreenComponent">
					<UIScreenComponent allowDpadNavigation="1" soundContext="" shortcutConfig="BACK_ONLY">
						<ENUM NAME="cursorActivation" SEL="0"/>
						<phoneSetupUiData>
							<PhoneSetupData isPopup="0" hasVisibleActions="0">
								<ENUM NAME="carouselBuild" SEL="2"/>
								<userFriendlyBindings VAL=""/>
							</PhoneSetupData>
						</phoneSetupUiData>
					</UIScreenComponent>
				</COMPONENTS>
				<COMPONENTS NAME="PropertyPatcher">
					<PropertyPatcher applyOnActivation="0"/>
				</COMPONENTS>
				<COMPONENTS NAME="TapeCase_Component">
					<TapeCase_Component/>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="banner" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/ui/components/ui.tpl" RELATIVEPATH="World/ui/screens/banners/default/item_song/song/default/banner.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="1">
				<MARKERS VAL="_MAP_BANNER"/>"
				<parentBind>
					<Bind parentPath="_map" typeData="0" offsetPos="0.000000 0.000000 3.000000" offsetAngle="0.000000" localScale="1.000000 1.000000" useParentFlip="1" useParentAlpha="0" useParentColor="0" removeWithParent="0">
						<ENUM NAME="type" SEL="0"/>
						<ENUM NAME="scaleInheritProp" SEL="2"/>
					</Bind>
				</parentBind>
				<COMPONENTS NAME="UIComponent">
					<UIComponent/>
				</COMPONENTS>
				<ENUM NAME="viewType" SEL="0"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="SubSceneActor">
			<SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="core_navigation" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/ui/components/ui.tpl" RELATIVEPATH="world/ui/screens/core_navigation/core_navigation.isc" EMBED_SCENE="0" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="1">
				<MARKERS VAL="_MAP_CORE_NAVIGATION"/>
				<parentBind>
					<Bind parentPath="_map" typeData="0" offsetPos="0.000000 0.000000 0.000000" offsetAngle="0.000000" localScale="1.000000 1.000000" useParentFlip="1" useParentAlpha="0" useParentColor="0" removeWithParent="0">
						<ENUM NAME="type" SEL="0"/>
						<ENUM NAME="scaleInheritProp" SEL="2"/>
					</Bind>
				</parentBind>
				<COMPONENTS NAME="UIComponent">
					<UIComponent/>
				</COMPONENTS>
				<ENUM NAME="viewType" SEL="0"/>
			</SubSceneActor>
		</ACTORS>
		<ACTORS NAME="Actor">
			<Actor RELATIVEZ="0.000122" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="ui_map_color_helper" POS2D="-4.003418 109.017403" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/ui/components/ui_map_color_helper.tpl">
				<parentBind>
					<Bind parentPath="_map" typeData="0" offsetPos="-4.003418 109.017403 0.000122" offsetAngle="0.000000" localScale="1.000000 1.000000" useParentFlip="1" useParentAlpha="0" useParentColor="0" removeWithParent="0">
						<ENUM NAME="type" SEL="0"/>
						<ENUM NAME="scaleInheritProp" SEL="2"/>
					</Bind>
				</parentBind>
				<COMPONENTS NAME="UIMapColorHelper">
					<UIMapColorHelper songBannerBkg_Path="world/MAPS/{mapName}/menuart/textures/{mapName}_banner_bkg.tga" songCoach_Path="world/MAPS/{mapName}/menuart/textures/{mapName}_Cover_AlbumCoach.tga" songColor_1A="0.100000 0.100000 0.100000 1.000000" songColor_1B="0.200000 0.200000 0.200000 1.000000" songColor_2A="0.800000 0.800000 0.800000 1.000000" songColor_2B="0.400000 0.400000 0.400000 1.000000">
					</UIMapColorHelper>
				</COMPONENTS>
			</Actor>
		</ACTORS>
		<sceneConfigs>
			<SceneConfigs activeSceneConfig="0">
				<sceneConfigs NAME="JD_MapSceneConfig">
					<JD_MapSceneConfig name="" soundContext="TitlePage" hud="0" phoneTitleLocId="4294967295" phoneImage="">
						<ENUM NAME="Pause_Level" SEL="6"/>
						<ENUM NAME="type" SEL="0"/>
						<ENUM NAME="musicscore" SEL="2"/>
					</JD_MapSceneConfig>
				</sceneConfigs>
			</SceneConfigs>
		</sceneConfigs>
	</Scene>
</root>
''')
    iscColorHelper.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/" + mapName + "_colorhelper.isc")

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
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic_kids" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic_kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
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
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic_kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
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
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic_kids" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic_kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
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
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic_kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
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
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic_kids" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic_kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
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
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic_kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
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
			<Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="{mapName}_cover_generic_kids" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="World/MAPS/{mapName}/menuart/actors/{mapName}_cover_generic_kids.act" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
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
									<GFXMaterialTexturePathSet diffuse="World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic_kids.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4=""/>
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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/" + mapName + "_MENUART.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_banner_bkg.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Coach.ignore")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Coach_1.act")

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
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Coach_2.act")

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
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Coach_3.act")

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
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Coach_4.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Cover_AlbumBkg.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Cover_AlbumCoach.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Cover_Generic.act")

    actCoverGenericKids = open(menuartActorsFolder + mapName + "_Cover_Generic_Kids.act", "w", encoding="utf-8")
    actCoverGenericKids.write(f'''params =
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
                                    diffuse = "World/MAPS/{mapName}/menuart/textures/{mapName}_cover_generic_kids.tga",

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
    actCoverGenericKids.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Cover_Generic_Kids.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Cover_Online.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_Cover_Online_Kids.act")

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
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Actors/" + mapName + "_map_bkg.act")

    # atlBannerBkg

    tfiBannerBkg = open(menuartTexturesFolder + mapName + "_banner_bkg.tga.tfi", "w", encoding="utf-8")
    tfiBannerBkg.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiBannerBkg.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_banner_bkg.tga.tfi")

    ignoreCoach = open(menuartTexturesFolder + mapName + "_Coach.ignore", "w", encoding="utf-8")
    ignoreCoach.write('''${if eq(NumberCoach, 1):
${MapName}$_Coach_2.atl
${MapName}$_Coach_2.tga
${MapName}$_Coach_2.tga.tfi
${MapName}$_Coach_2_Phone.png
${MapName}$_Coach_2_Phone.png.tfi
${MapName}$_Coach_3.atl
${MapName}$_Coach_3.tga
${MapName}$_Coach_3.tga.tfi
${MapName}$_Coach_3_Phone.png
${MapName}$_Coach_3_Phone.png.tfi
${MapName}$_Coach_4.atl
${MapName}$_Coach_4.tga
${MapName}$_Coach_4.tga.tfi
${MapName}$_Coach_4_Phone.png
${MapName}$_Coach_4_Phone.png.tfi
}$

${if eq(NumberCoach, 2):
${MapName}$_Coach_3.atl
${MapName}$_Coach_3.tga
${MapName}$_Coach_3.tga.tfi
${MapName}$_Coach_3_Phone.png
${MapName}$_Coach_3_Phone.png.tfi
${MapName}$_Coach_4.atl
${MapName}$_Coach_4.tga
${MapName}$_Coach_4.tga.tfi
${MapName}$_Coach_4_Phone.png
${MapName}$_Coach_4_Phone.png.tfi
}$

${if eq(NumberCoach, 3):
${MapName}$_Coach_4.atl
${MapName}$_Coach_4.tga
${MapName}$_Coach_4.tga.tfi
${MapName}$_Coach_4_Phone.png
${MapName}$_Coach_4_Phone.png.tfi
}$''')
    ignoreCoach.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach.ignore")

    atlCoachesContent = f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=1024,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
'''

    tfiCoachesContent = f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>'''

    tfiCoachesPhoneContent = f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="NONE" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="NONE" />
  <TextureConfiguration TargetName="X360" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PS3" CompressionMode="NONE" />
  <TextureConfiguration TargetName="WII" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PC" CompressionMode="NONE" />
  <TextureConfiguration TargetName="NX" CompressionMode="NONE" />
  <TextureConfiguration TargetName="GGP" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="NONE" />
</root>'''

    atlCoach1 = open(menuartTexturesFolder + mapName + "_Coach_1.atl", "w", encoding="utf-8")
    atlCoach1.write(atlCoachesContent)
    atlCoach1.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_1.atl")

    tfiCoach1 = open(menuartTexturesFolder + mapName + "_Coach_1.tga.tfi", "w", encoding="utf-8")
    tfiCoach1.write(tfiCoachesContent)
    tfiCoach1.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_1.tga.tfi")

    tfiCoachPhone1 = open(menuartTexturesFolder + mapName + "_Coach_1_Phone.png.tfi", "w", encoding="utf-8")
    tfiCoachPhone1.write(tfiCoachesPhoneContent)
    tfiCoachPhone1.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_1_Phone.png.tfi")

    if coachNumber > 1:
        atlCoach2 = open(menuartTexturesFolder + mapName + "_Coach_2.atl", "w", encoding="utf-8")
        atlCoach2.write(atlCoachesContent)
        atlCoach2.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_2.atl")

        tfiCoach2 = open(menuartTexturesFolder + mapName + "_Coach_2.tga.tfi", "w", encoding="utf-8")
        tfiCoach2.write(tfiCoachesContent)
        tfiCoach2.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_2.tga.tfi")

        tfiCoachPhone2 = open(menuartTexturesFolder + mapName + "_Coach_2_Phone.png.tfi", "w", encoding="utf-8")
        tfiCoachPhone2.write(tfiCoachesPhoneContent)
        tfiCoachPhone2.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_2_Phone.png.tfi")

    if coachNumber > 2:
        atlCoach3 = open(menuartTexturesFolder + mapName + "_Coach_3.atl", "w", encoding="utf-8")
        atlCoach3.write(atlCoachesContent)
        atlCoach3.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_3.atl")

        tfiCoach3 = open(menuartTexturesFolder + mapName + "_Coach_3.tga.tfi", "w", encoding="utf-8")
        tfiCoach3.write(tfiCoachesContent)
        tfiCoach3.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_3.tga.tfi")

        tfiCoachPhone3 = open(menuartTexturesFolder + mapName + "_Coach_3_Phone.png.tfi", "w", encoding="utf-8")
        tfiCoachPhone3.write(tfiCoachesPhoneContent)
        tfiCoachPhone3.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_3_Phone.png.tfi")

    if coachNumber > 3:
        atlCoach4 = open(menuartTexturesFolder + mapName + "_Coach_4.atl", "w", encoding="utf-8")
        atlCoach4.write(atlCoachesContent)
        atlCoach4.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_4.atl")

        tfiCoach4 = open(menuartTexturesFolder + mapName + "_Coach_4.tga.tfi", "w", encoding="utf-8")
        tfiCoach4.write(tfiCoachesContent)
        tfiCoach4.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_4.tga.tfi")

        tfiCoachPhone4 = open(menuartTexturesFolder + mapName + "_Coach_4_Phone.png.tfi", "w", encoding="utf-8")
        tfiCoachPhone4.write(tfiCoachesPhoneContent)
        tfiCoachPhone4.close()
        print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Coach_4_Phone.png.tfi")

    tfiCover = open(menuartTexturesFolder + mapName + "_Cover.jpg.tfi", "w", encoding="utf-8")
    tfiCover.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="NONE" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="NONE" />
  <TextureConfiguration TargetName="X360" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PS3" CompressionMode="NONE" />
  <TextureConfiguration TargetName="WII" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PC" CompressionMode="NONE" />
  <TextureConfiguration TargetName="NX" CompressionMode="NONE" />
  <TextureConfiguration TargetName="GGP" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="NONE" />
</root>''')
    tfiCover.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover.jpg.tfi")

    tfiCover2x = open(menuartTexturesFolder + mapName + "_Cover_2x.jpg.tfi", "w", encoding="utf-8")
    tfiCover2x.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="NONE" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="NONE" />
  <TextureConfiguration TargetName="X360" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PS3" CompressionMode="NONE" />
  <TextureConfiguration TargetName="WII" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PC" CompressionMode="NONE" />
  <TextureConfiguration TargetName="NX" CompressionMode="NONE" />
  <TextureConfiguration TargetName="GGP" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="NONE" />
</root>''')
    tfiCover2x.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_2x.jpg.tfi")

    tfiCover1024 = open(menuartTexturesFolder + mapName + "_Cover_1024.tga.tfi", "w", encoding="utf-8")
    tfiCover1024.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiCover1024.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_1024.tga.tfi")

    atlAlbumBkg = open(menuartTexturesFolder + mapName + "_Cover_AlbumBkg.atl", "w", encoding="utf-8")
    atlAlbumBkg.write(f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=1024,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
''')
    atlAlbumBkg.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_AlbumBkg.atl")

    tfiAlbumBkg = open(menuartTexturesFolder + mapName + "_Cover_AlbumBkg.tga.tfi", "w", encoding="utf-8")
    tfiAlbumBkg.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiAlbumBkg.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_AlbumBkg.tga.tfi")

    atlCoverAlbumCoach = open(menuartTexturesFolder + mapName + "_Cover_AlbumCoach.atl", "w", encoding="utf-8")
    atlCoverAlbumCoach.write(f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=1024,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
''')
    atlCoverAlbumCoach.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_AlbumCoach.atl")

    tfiCoverAlbumCoach = open(menuartTexturesFolder + mapName + "_Cover_AlbumCoach.tga.tfi", "w", encoding="utf-8")
    tfiCoverAlbumCoach.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiCoverAlbumCoach.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_AlbumCoach.tga.tfi")

    atlCoverGeneric = open(menuartTexturesFolder + mapName + "_Cover_Generic.atl", "w", encoding="utf-8")
    atlCoverGeneric.write(f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=1024,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
''')
    atlCoverGeneric.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Generic.atl")

    tfiCoverGeneric = open(menuartTexturesFolder + mapName + "_Cover_Generic.tga.tfi", "w", encoding="utf-8")
    tfiCoverGeneric.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiCoverGeneric.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Generic.tga.tfi")

    atlCoverGenericKids = open(menuartTexturesFolder + mapName + "_Cover_Generic_Kids.atl", "w", encoding="utf-8")
    atlCoverGenericKids.write(f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=1024,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
''')
    atlCoverGenericKids.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Generic_Kids.atl")

    tfiCoverGenericKids = open(menuartTexturesFolder + mapName + "_Cover_Generic_Kids.tga.tfi", "w", encoding="utf-8")
    tfiCoverGenericKids.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="1" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiCoverGenericKids.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Generic_Kids.tga.tfi")

    atlCoverOnline = open(menuartTexturesFolder + mapName + "_Cover_Online.atl", "w", encoding="utf-8")
    atlCoverOnline.write(f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=256,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
''')
    atlCoverOnline.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Online.atl")

    tfiCoverOnline = open(menuartTexturesFolder + mapName + "_Cover_Online.tga.tfi", "w", encoding="utf-8")
    tfiCoverOnline.write(f'''<root>
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiCoverOnline.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Online.tga.tfi")

    atlCoverOnlineKids = open(menuartTexturesFolder + mapName + "_Cover_Online_Kids.atl", "w", encoding="utf-8")
    atlCoverOnlineKids.write(f'''ITF_GFX_UV_ATLAS =
{{
	TextureHeight=256,
	TextureAspectRatio=1,
    {{
        index=0,
        uvNumber=4,
        uv0=vector2dNew(0,0),
        uv1=vector2dNew(1,0),
        uv2=vector2dNew(1,1),
        uv3=vector2dNew(0,1),
    }},
}}
''')
    atlCoverOnlineKids.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Online_Kids.atl")

    tfiCoverOnlineKids = open(menuartTexturesFolder + mapName + "_Cover_Online_Kids.tga.tfi", "w", encoding="utf-8")
    tfiCoverOnlineKids.write(f'''<root>
  <TextureConfiguration TargetName="X360" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PS3" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="WII" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT5" MipmapLevelStart="2" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiCoverOnlineKids.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Online_Kids.tga.tfi")

    tfiCoverPhone = open(menuartTexturesFolder + mapName + "_Cover_Phone.jpg.tfi", "w", encoding="utf-8")
    tfiCoverPhone.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="NONE" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="NONE" />
  <TextureConfiguration TargetName="X360" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PS3" CompressionMode="NONE" />
  <TextureConfiguration TargetName="WII" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PC" CompressionMode="NONE" />
  <TextureConfiguration TargetName="NX" CompressionMode="NONE" />
  <TextureConfiguration TargetName="GGP" CompressionMode="NONE" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="NONE" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="NONE" />
</root>''')
    tfiCoverPhone.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_Cover_Phone.jpg.tfi")

    # atlMapBkg

    tfiMapBkg = open(menuartTexturesFolder + mapName + "_map_bkg.tga.tfi", "w", encoding="utf-8")
    tfiMapBkg.write(f'''<root>
  <TextureConfiguration TargetName="DURANGO" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="ORBIS" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="CAFE" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PC" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="NX" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="GGP" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="PROSPERO" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
  <TextureConfiguration TargetName="SCARLETT" CompressionMode="DXT1" MipmapLevelStart="0" UseMipmap="False" WrapModeX="WrapMode_Repeat" WrapModeY="WrapMode_Repeat" Filter="MipmapFilter_Box" AllowDegradation="False" LodBias="0" AllowDegradationAlpha="False" OneColMode="auto" Anisotropy="max" />
</root>''')
    tfiMapBkg.close()
    print("\033[32mDONE\033[0m", mapName + "/MenuArt/Textures/" + mapName + "_map_bkg.tga.tfi")

    #Timeline files
    btape = open(timelineFolder + mapName + ".btape", "w", encoding="utf-8")
    btape.write(f'''params =
{{
    NAME = "Tape",
    Tape = 
    {{
        TapeClock = 2, -- TapeClock_Engine
        TapeBarCount = 1,
        FreeResourcesAfterPlay = 0,
        MapName = "{mapName}",
        SoundwichEvent = "",
    }},
}}
''')
    btape.close()
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + ".btape")

    lyrics = open(timelineFolder + mapName + "_Lyrics.txt", "w", encoding="utf-8")
    lyrics.write("")
    lyrics.close()
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_Lyrics.txt")

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
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML_Dance.act")

    tapeTmlDance = open(timelineFolder + mapName + "_TML_Dance.dtape", "w", encoding="utf-8")
    tapeTmlDance.write(f'''params =
{{
    NAME = "Tape",
    Tape = 
    {{
        TapeClock = 0, -- TapeClock_ConductorGameplay
        TapeBarCount = 1,
        FreeResourcesAfterPlay = 0,
        MapName = "{mapName}",
        SoundwichEvent = "",
    }},
}}
''')
    tapeTmlDance.close()
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML_Dance.dtape")

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
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML_Dance.tpl")

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
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML_Karaoke.act")

    tapeTmlKaraoke = open(timelineFolder + mapName + "_TML_Karaoke.ktape", "w", encoding="utf-8")
    tapeTmlKaraoke.write(f'''params =
{{
    NAME = "Tape",
    Tape = 
    {{
        TapeClock = 0, -- TapeClock_ConductorGameplay
        TapeBarCount = 1,
        FreeResourcesAfterPlay = 0,
        MapName = "{mapName}",
        SoundwichEvent = "",
    }},
}}
''')
    tapeTmlKaraoke.close()
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML_Karaoke.ktape")

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
    print("\033[32mDONE\033[0m", mapName + "/Timeline/" + mapName + "_TML_Karaoke.tpl")

    #VideosCoach files
    mpdHD = open(videoscoachFolder + mapName + ".hd.mpd", "w", encoding="utf-8")
    mpdHD.write(f'''<?xml version="1.0"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011" xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011" type="static" mediaPresentationDuration="PT50.919998S" minBufferTime="PT1S" profiles="urn:webm:dash:profile:webm-on-demand:2012"/>
''')
    mpdHD.close()
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + ".hd.mpd")

    mpd = open(videoscoachFolder + mapName + ".mpd", "w", encoding="utf-8")
    mpd.write(f'''<?xml version="1.0"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011" xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011" type="static" mediaPresentationDuration="PT50.919998S" minBufferTime="PT1S" profiles="urn:webm:dash:profile:webm-on-demand:2012"/>
''')
    mpd.close()
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + ".mpd")

    mpdVP9 = open(videoscoachFolder + mapName + ".vp9.mpd", "w", encoding="utf-8")
    mpdVP9.write(f'''<?xml version="1.0"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011" xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011" type="static" mediaPresentationDuration="PT50.919998S" minBufferTime="PT1S" profiles="urn:webm:dash:profile:webm-on-demand:2012"/>
''')
    mpdVP9.close()
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + ".vp9.mpd")

    mpdMapPreviewNoSoundCropVP8 = open(videoscoachFolder + mapName + "_MapPreviewNoSoundCrop.vp8.mpd", "w", encoding="utf-8")
    mpdMapPreviewNoSoundCropVP8.write(f'''<?xml version="1.0"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011" xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011" type="static" mediaPresentationDuration="PT30S" minBufferTime="PT1S" profiles="urn:webm:dash:profile:webm-on-demand:2012"/>
''')
    mpdMapPreviewNoSoundCropVP8.close()
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + "_MapPreviewNoSoundCrop.vp8.mpd")

    mpdMapPreviewNoSoundCropVP9 = open(videoscoachFolder + mapName + "_MapPreviewNoSoundCrop.vp9.mpd", "w", encoding="utf-8")
    mpdMapPreviewNoSoundCropVP9.write(f'''<?xml version="1.0"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:DASH:schema:MPD:2011" xsi:schemaLocation="urn:mpeg:DASH:schema:MPD:2011" type="static" mediaPresentationDuration="PT30S" minBufferTime="PT1S" profiles="urn:webm:dash:profile:webm-on-demand:2012"/>
''')
    mpdMapPreviewNoSoundCropVP9.close()
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + "_MapPreviewNoSoundCrop.vp9.mpd")

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
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + "_VIDEO.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + mapName + "_VIDEO_MAP_PREVIEW.isc")

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
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + "video_player_main.act")

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
    print("\033[32mDONE\033[0m", mapName + "/VideosCoach/" + "video_player_map_preview.act")

    #TEMPLATE.txt files
    shutil.copyfile("assets/TEMPLATE.txt", rawDataMenuArt + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", durangoMovesFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", orbisMovesFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", ps3MovesFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", wiiMovesFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", wiiuMovesFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", x360MovesFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", timelinePictosFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", rawDataPictos + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", timelineRecordingFolder + "TEMPLATE.txt")
    shutil.copyfile("assets/TEMPLATE.txt", timelineSnippingFolder + "TEMPLATE.txt")
    print("\033[32mDONE\033[0m", "Copied all TEMPLATE.txt files...")

except Exception as e:
    print(f"\033[31mERROR:\033[0m {e}")
