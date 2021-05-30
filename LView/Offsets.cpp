#include "Offsets.h"

Offsets::Offsets() {};

int Offsets::GameTime = 0x2FA0294; //		11.9 ==> 11.10
//int Offsets::GameVersion = 0x2FC8230; //		11.9 ==> 11.10

int Offsets::ObjIndex = 0x20; //			UNCHANGED
int Offsets::ObjTeam = 0x4C; //			UNCHANGED
int Offsets::ObjNetworkID = 0xCC; //			UNCHANGED
int Offsets::ObjPos = 0x1d8; //			UNCHANGED
int Offsets::ObjVisibility = 0x270; //			UNCHANGED
int Offsets::ObjSpawnCount = 0x284; //			UNCHANGED
int Offsets::ObjSrcIndex = 0x290; //			UNCHANGED
int Offsets::ObjMana = 0x298; //			UNCHANGED
int Offsets::ObjHealth = 0xD98; //			UNCHANGED
int Offsets::ObjMaxHealth = 0xDA8; //			UNCHANGED
//int Offsets::ObjRecall = 0xD8C; //			UNCHANGED
int Offsets::ObjArmor = 0x12C8; //		11.9 ==> 11.10
int Offsets::ObjMagicRes = 0x12D0; //		11.9 ==> 11.10
int Offsets::ObjBaseAtk = 0x12A0; //		11.9 ==> 11.10
int Offsets::ObjBonusAtk = 0x1218; //		UNCHANGED
int Offsets::ObjMoveSpeed = 0x12E0; //		11.9 ==> 11.10
int Offsets::ObjSpellBook = 0x2880; //		11.9 ==> 11.10 0x2408
int Offsets::ObjName = 0x2C74; //		11.10: 0x2E3C
int Offsets::ObjLvl = 0x33E0; //		11.9 ==> 11.10
int Offsets::ObjExpiry = 0x298; //			UNCHANGED
int Offsets::ObjCrit = 0x12C4; //		11.9 ==> 11.10
int Offsets::ObjCritMulti = 0x12B4; //		11.9 ==> 11.10
int Offsets::ObjAbilityPower = 0x1228; //		UNCHANGED
int Offsets::ObjAtkSpeedMulti = 0x129C; //		11.9 ==> 11.10
int Offsets::ObjItemList = 0x3430; //		NOT SURE
//int Offsets::ObjExpierience = 0x33CC; //		11.9 ==> 11.10

int Offsets::ItemListItem = 0xC; //			NOT TOUCHED
int Offsets::ItemInfo = 0x20; //			NOT TOUCHED
int Offsets::ItemInfoId = 0x68; //			NOT TOUCHED

int Offsets::ViewProjMatrices = 0x2FCBAA0; //		11.9 ==> 11.10
int Offsets::Renderer = 0x2FCE914; //		11.9 ==> 11.10 
int Offsets::RendererWidth = 0x0C; //			UNCHANGED
int Offsets::RendererHeight = 0x10; //			UNCHANGED

int Offsets::SpellSlotLevel = 0x20; //			UNCHANGED
int Offsets::SpellSlotTime = 0x28; //			UNCHANGED
int Offsets::SpellSlotDamage = 0x94; //			UNCHANGED
int Offsets::SpellSlotSpellInfo = 0x13C; //			UNCHANGED
int Offsets::SpellInfoSpellData = 0x44; //			UNCHANGED
int Offsets::SpellDataSpellName = 0x6C; //			11.9 ==> 11.10
int Offsets::SpellDataMissileName = 0x6C; //			11.9 ==> 11.10
//int Offsets::SpellSlotSmiteTimer = 0x64; //			UNCHANGED
//int Offsets::SpellSlotSmiteCharges = 0x58; //			UNCHANGED

int Offsets::ObjectManager = 0x0170bbb8; //		11.9 ==> 11.10
int Offsets::LocalPlayer = 0x02fa7fe0; //		11.9 ==> 11.10
int Offsets::UnderMouseObject = 0x02fa89f8; //		11.9 ==> 11.10 11.11: 0x2fb6218
int Offsets::ObjectMapCount = 0x2C; //			UNCHANGED
int Offsets::ObjectMapRoot = 0x28; //			UNCHANGED
int Offsets::ObjectMapNodeNetId = 0x10; //			UNCHANGED
int Offsets::ObjectMapNodeObject = 0x14; //			UNCHANGED

int Offsets::MissileSpellInfo = 0x258; //			UNCHANGED
int Offsets::MissileSrcIdx = 0x2B8; //			UNCHANGED
int Offsets::MissileDestIdx = 0x310; //			UNCHANGED
int Offsets::MissileStartPos = 0x2D0; //			UNCHANGED
int Offsets::MissileEndPos = 0x2DC; //			UNCHANGED
//int Offsets::MissileCurrentPos = 0x220;//			NEW

int Offsets::MinimapObject = 0x02fc643c; //		11.9 ==> 11.10 11: 0x02fc643c

int Offsets::MinimapObjectHud = 0x88; //			UNCHANGED
int Offsets::MinimapHudPos = 0x60; //			UNCHANGED
int Offsets::MinimapHudSize = 0x68; //			UNCHANGED