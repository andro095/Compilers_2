// Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/backend/MyModules/YAPL/Yapl.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YaplParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, ELSE=2, FI=3, IF=4, IN=5, INHERITS=6, ISVOID=7, LOOP=8, POOL=9, 
		THEN=10, WHILE=11, NEW=12, NOT=13, LET=14, FALSE=15, TRUE=16, SEMICOLON=17, 
		LCURLY=18, RCURLY=19, LSQUARE=20, RSQUARE=21, LROUND=22, RROUND=23, COMMA=24, 
		POINT=25, QUOTES=26, APOSTROPHE=27, ADD=28, SUB=29, MULTIPLY=30, DIVIDE=31, 
		INT_NOT=32, COLON=33, ASIGN=34, ARROBA=35, LESS_THAN=36, LESS_EQUAL=37, 
		EQUAL=38, LINE_COMMENT=39, COMMENT=40, INTEGER=41, STRING=42, TYPE=43, 
		ID=44, WS=45;
	public static final int
		RULE_program = 0, RULE_class = 1, RULE_feature = 2, RULE_formal = 3, RULE_expr = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class", "feature", "formal", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "'false'", "'true'", "';'", "'{'", "'}'", "'['", "']'", 
			"'('", "')'", "','", "'.'", "'\"'", "'''", "'+'", "'-'", "'*'", "'/'", 
			"'~'", "':'", "'<-'", "'@'", "'<'", "'<='", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", 
			"POOL", "THEN", "WHILE", "NEW", "NOT", "LET", "FALSE", "TRUE", "SEMICOLON", 
			"LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", "RROUND", "COMMA", 
			"POINT", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
			"INT_NOT", "COLON", "ASIGN", "ARROBA", "LESS_THAN", "LESS_EQUAL", "EQUAL", 
			"LINE_COMMENT", "COMMENT", "INTEGER", "STRING", "TYPE", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Yapl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YaplParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<ClassContext> class() {
			return getRuleContexts(ClassContext.class);
		}
		public ClassContext class(int i) {
			return getRuleContext(ClassContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YaplParser.SEMICOLON, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				class();
				setState(11);
				match(SEMICOLON);
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(YaplParser.CLASS, 0); }
		public List<TerminalNode> TYPE() { return getTokens(YaplParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YaplParser.TYPE, i);
		}
		public TerminalNode LCURLY() { return getToken(YaplParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(YaplParser.RCURLY, 0); }
		public TerminalNode INHERITS() { return getToken(YaplParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YaplParser.SEMICOLON, i);
		}
		public ClassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class; }
	}

	public final ClassContext class() throws RecognitionException {
		ClassContext _localctx = new ClassContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			match(CLASS);
			setState(18);
			match(TYPE);
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(19);
				match(INHERITS);
				setState(20);
				match(TYPE);
				}
			}

			setState(23);
			match(LCURLY);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(24);
				feature();
				setState(25);
				match(SEMICOLON);
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YaplParser.ID, 0); }
		public TerminalNode LROUND() { return getToken(YaplParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(YaplParser.RROUND, 0); }
		public TerminalNode COLON() { return getToken(YaplParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YaplParser.TYPE, 0); }
		public TerminalNode LCURLY() { return getToken(YaplParser.LCURLY, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RCURLY() { return getToken(YaplParser.RCURLY, 0); }
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YaplParser.COMMA, i);
		}
		public TerminalNode ASIGN() { return getToken(YaplParser.ASIGN, 0); }
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(60);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(ID);
				setState(35);
				match(LROUND);
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(36);
					formal();
					setState(41);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(37);
						match(COMMA);
						setState(38);
						formal();
						}
						}
						setState(43);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(46);
				match(RROUND);
				setState(47);
				match(COLON);
				setState(48);
				match(TYPE);
				setState(49);
				match(LCURLY);
				setState(50);
				expr(0);
				setState(51);
				match(RCURLY);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				match(ID);
				setState(54);
				match(COLON);
				setState(55);
				match(TYPE);
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGN) {
					{
					setState(56);
					match(ASIGN);
					setState(57);
					expr(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YaplParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YaplParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YaplParser.TYPE, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(ID);
			setState(63);
			match(COLON);
			setState(64);
			match(TYPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(YaplParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(YaplParser.ID, i);
		}
		public List<TerminalNode> ASIGN() { return getTokens(YaplParser.ASIGN); }
		public TerminalNode ASIGN(int i) {
			return getToken(YaplParser.ASIGN, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LROUND() { return getToken(YaplParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(YaplParser.RROUND, 0); }
		public List<TerminalNode> COMMA() { return getTokens(YaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YaplParser.COMMA, i);
		}
		public TerminalNode IF() { return getToken(YaplParser.IF, 0); }
		public TerminalNode THEN() { return getToken(YaplParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YaplParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YaplParser.FI, 0); }
		public TerminalNode WHILE() { return getToken(YaplParser.WHILE, 0); }
		public TerminalNode LOOP() { return getToken(YaplParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YaplParser.POOL, 0); }
		public TerminalNode LCURLY() { return getToken(YaplParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(YaplParser.RCURLY, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(YaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YaplParser.SEMICOLON, i);
		}
		public TerminalNode LET() { return getToken(YaplParser.LET, 0); }
		public List<TerminalNode> COLON() { return getTokens(YaplParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(YaplParser.COLON, i);
		}
		public List<TerminalNode> TYPE() { return getTokens(YaplParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YaplParser.TYPE, i);
		}
		public TerminalNode IN() { return getToken(YaplParser.IN, 0); }
		public TerminalNode NEW() { return getToken(YaplParser.NEW, 0); }
		public TerminalNode ISVOID() { return getToken(YaplParser.ISVOID, 0); }
		public TerminalNode INT_NOT() { return getToken(YaplParser.INT_NOT, 0); }
		public TerminalNode NOT() { return getToken(YaplParser.NOT, 0); }
		public TerminalNode INTEGER() { return getToken(YaplParser.INTEGER, 0); }
		public TerminalNode STRING() { return getToken(YaplParser.STRING, 0); }
		public TerminalNode TRUE() { return getToken(YaplParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(YaplParser.FALSE, 0); }
		public TerminalNode ADD() { return getToken(YaplParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(YaplParser.SUB, 0); }
		public TerminalNode MULTIPLY() { return getToken(YaplParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(YaplParser.DIVIDE, 0); }
		public TerminalNode LESS_THAN() { return getToken(YaplParser.LESS_THAN, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(YaplParser.LESS_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(YaplParser.EQUAL, 0); }
		public TerminalNode POINT() { return getToken(YaplParser.POINT, 0); }
		public TerminalNode ARROBA() { return getToken(YaplParser.ARROBA, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(67);
				match(ID);
				setState(68);
				match(ASIGN);
				setState(69);
				expr(24);
				}
				break;
			case 2:
				{
				setState(70);
				match(ID);
				setState(71);
				match(LROUND);
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0)) {
					{
					setState(72);
					expr(0);
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(73);
						match(COMMA);
						setState(74);
						expr(0);
						}
						}
						setState(79);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(82);
				match(RROUND);
				}
				break;
			case 3:
				{
				setState(83);
				match(IF);
				setState(84);
				expr(0);
				setState(85);
				match(THEN);
				setState(86);
				expr(0);
				setState(87);
				match(ELSE);
				setState(88);
				expr(0);
				setState(89);
				match(FI);
				}
				break;
			case 4:
				{
				setState(91);
				match(WHILE);
				setState(92);
				expr(0);
				setState(93);
				match(LOOP);
				setState(94);
				expr(0);
				setState(95);
				match(POOL);
				}
				break;
			case 5:
				{
				setState(97);
				match(LCURLY);
				setState(101); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(98);
					expr(0);
					setState(99);
					match(SEMICOLON);
					}
					}
					setState(103); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0) );
				setState(105);
				match(RCURLY);
				}
				break;
			case 6:
				{
				setState(107);
				match(LET);
				setState(108);
				match(ID);
				setState(109);
				match(COLON);
				setState(110);
				match(TYPE);
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGN) {
					{
					setState(111);
					match(ASIGN);
					setState(112);
					expr(0);
					}
				}

				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(115);
					match(COMMA);
					setState(116);
					match(ID);
					setState(117);
					match(COLON);
					setState(118);
					match(TYPE);
					setState(121);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==ASIGN) {
						{
						setState(119);
						match(ASIGN);
						setState(120);
						expr(0);
						}
					}

					}
					}
					setState(127);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(128);
				match(IN);
				setState(129);
				expr(18);
				}
				break;
			case 7:
				{
				setState(130);
				match(NEW);
				setState(131);
				match(TYPE);
				}
				break;
			case 8:
				{
				setState(132);
				match(ISVOID);
				setState(133);
				expr(16);
				}
				break;
			case 9:
				{
				setState(134);
				match(INT_NOT);
				setState(135);
				expr(11);
				}
				break;
			case 10:
				{
				setState(136);
				match(NOT);
				setState(137);
				expr(7);
				}
				break;
			case 11:
				{
				setState(138);
				match(LROUND);
				setState(139);
				expr(0);
				setState(140);
				match(RROUND);
				}
				break;
			case 12:
				{
				setState(142);
				match(ID);
				}
				break;
			case 13:
				{
				setState(143);
				match(INTEGER);
				}
				break;
			case 14:
				{
				setState(144);
				match(STRING);
				}
				break;
			case 15:
				{
				setState(145);
				match(TRUE);
				}
				break;
			case 16:
				{
				setState(146);
				match(FALSE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(191);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(189);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(149);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(150);
						match(ADD);
						setState(151);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(152);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(153);
						match(SUB);
						setState(154);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(155);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(156);
						match(MULTIPLY);
						setState(157);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(158);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(159);
						match(DIVIDE);
						setState(160);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(161);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(162);
						match(LESS_THAN);
						setState(163);
						expr(11);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(164);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(165);
						match(LESS_EQUAL);
						setState(166);
						expr(10);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(167);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(168);
						match(EQUAL);
						setState(169);
						expr(9);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(170);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(173);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==ARROBA) {
							{
							setState(171);
							match(ARROBA);
							setState(172);
							match(TYPE);
							}
						}

						setState(175);
						match(POINT);
						setState(176);
						match(ID);
						setState(177);
						match(LROUND);
						setState(186);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0)) {
							{
							setState(178);
							expr(0);
							setState(183);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(179);
								match(COMMA);
								setState(180);
								expr(0);
								}
								}
								setState(185);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(188);
						match(RROUND);
						}
						break;
					}
					} 
				}
				setState(193);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		case 7:
			return precpred(_ctx, 23);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/\u00c5\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\6\2\20\n\2\r\2\16\2\21\3\3"+
		"\3\3\3\3\3\3\5\3\30\n\3\3\3\3\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\3"+
		"\3\3\3\4\3\4\3\4\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\5\4/\n\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\5\4?\n\4\3\5\3\5\3\5\3\5"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6N\n\6\f\6\16\6Q\13\6\5\6S\n\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\6\6h\n\6\r\6\16\6i\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6t\n\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\5\6|\n\6\7\6~\n\6\f\6\16\6\u0081\13\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0096"+
		"\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b0\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7"+
		"\6\u00b8\n\6\f\6\16\6\u00bb\13\6\5\6\u00bd\n\6\3\6\7\6\u00c0\n\6\f\6\16"+
		"\6\u00c3\13\6\3\6\2\3\n\7\2\4\6\b\n\2\2\2\u00e6\2\17\3\2\2\2\4\23\3\2"+
		"\2\2\6>\3\2\2\2\b@\3\2\2\2\n\u0095\3\2\2\2\f\r\5\4\3\2\r\16\7\23\2\2\16"+
		"\20\3\2\2\2\17\f\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22"+
		"\3\3\2\2\2\23\24\7\3\2\2\24\27\7-\2\2\25\26\7\b\2\2\26\30\7-\2\2\27\25"+
		"\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\37\7\24\2\2\32\33\5\6\4\2\33\34"+
		"\7\23\2\2\34\36\3\2\2\2\35\32\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3"+
		"\2\2\2 \"\3\2\2\2!\37\3\2\2\2\"#\7\25\2\2#\5\3\2\2\2$%\7.\2\2%.\7\30\2"+
		"\2&+\5\b\5\2\'(\7\32\2\2(*\5\b\5\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3"+
		"\2\2\2,/\3\2\2\2-+\3\2\2\2.&\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\7\31"+
		"\2\2\61\62\7#\2\2\62\63\7-\2\2\63\64\7\24\2\2\64\65\5\n\6\2\65\66\7\25"+
		"\2\2\66?\3\2\2\2\678\7.\2\289\7#\2\29<\7-\2\2:;\7$\2\2;=\5\n\6\2<:\3\2"+
		"\2\2<=\3\2\2\2=?\3\2\2\2>$\3\2\2\2>\67\3\2\2\2?\7\3\2\2\2@A\7.\2\2AB\7"+
		"#\2\2BC\7-\2\2C\t\3\2\2\2DE\b\6\1\2EF\7.\2\2FG\7$\2\2G\u0096\5\n\6\32"+
		"HI\7.\2\2IR\7\30\2\2JO\5\n\6\2KL\7\32\2\2LN\5\n\6\2MK\3\2\2\2NQ\3\2\2"+
		"\2OM\3\2\2\2OP\3\2\2\2PS\3\2\2\2QO\3\2\2\2RJ\3\2\2\2RS\3\2\2\2ST\3\2\2"+
		"\2T\u0096\7\31\2\2UV\7\6\2\2VW\5\n\6\2WX\7\f\2\2XY\5\n\6\2YZ\7\4\2\2Z"+
		"[\5\n\6\2[\\\7\5\2\2\\\u0096\3\2\2\2]^\7\r\2\2^_\5\n\6\2_`\7\n\2\2`a\5"+
		"\n\6\2ab\7\13\2\2b\u0096\3\2\2\2cg\7\24\2\2de\5\n\6\2ef\7\23\2\2fh\3\2"+
		"\2\2gd\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\25\2\2l\u0096"+
		"\3\2\2\2mn\7\20\2\2no\7.\2\2op\7#\2\2ps\7-\2\2qr\7$\2\2rt\5\n\6\2sq\3"+
		"\2\2\2st\3\2\2\2t\177\3\2\2\2uv\7\32\2\2vw\7.\2\2wx\7#\2\2x{\7-\2\2yz"+
		"\7$\2\2z|\5\n\6\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}u\3\2\2\2~\u0081\3\2\2"+
		"\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2"+
		"\2\u0082\u0083\7\7\2\2\u0083\u0096\5\n\6\24\u0084\u0085\7\16\2\2\u0085"+
		"\u0096\7-\2\2\u0086\u0087\7\t\2\2\u0087\u0096\5\n\6\22\u0088\u0089\7\""+
		"\2\2\u0089\u0096\5\n\6\r\u008a\u008b\7\17\2\2\u008b\u0096\5\n\6\t\u008c"+
		"\u008d\7\30\2\2\u008d\u008e\5\n\6\2\u008e\u008f\7\31\2\2\u008f\u0096\3"+
		"\2\2\2\u0090\u0096\7.\2\2\u0091\u0096\7+\2\2\u0092\u0096\7,\2\2\u0093"+
		"\u0096\7\22\2\2\u0094\u0096\7\21\2\2\u0095D\3\2\2\2\u0095H\3\2\2\2\u0095"+
		"U\3\2\2\2\u0095]\3\2\2\2\u0095c\3\2\2\2\u0095m\3\2\2\2\u0095\u0084\3\2"+
		"\2\2\u0095\u0086\3\2\2\2\u0095\u0088\3\2\2\2\u0095\u008a\3\2\2\2\u0095"+
		"\u008c\3\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2"+
		"\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u00c1\3\2\2\2\u0097"+
		"\u0098\f\21\2\2\u0098\u0099\7\36\2\2\u0099\u00c0\5\n\6\22\u009a\u009b"+
		"\f\20\2\2\u009b\u009c\7\37\2\2\u009c\u00c0\5\n\6\21\u009d\u009e\f\17\2"+
		"\2\u009e\u009f\7 \2\2\u009f\u00c0\5\n\6\20\u00a0\u00a1\f\16\2\2\u00a1"+
		"\u00a2\7!\2\2\u00a2\u00c0\5\n\6\17\u00a3\u00a4\f\f\2\2\u00a4\u00a5\7&"+
		"\2\2\u00a5\u00c0\5\n\6\r\u00a6\u00a7\f\13\2\2\u00a7\u00a8\7\'\2\2\u00a8"+
		"\u00c0\5\n\6\f\u00a9\u00aa\f\n\2\2\u00aa\u00ab\7(\2\2\u00ab\u00c0\5\n"+
		"\6\13\u00ac\u00af\f\31\2\2\u00ad\u00ae\7%\2\2\u00ae\u00b0\7-\2\2\u00af"+
		"\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\7\33"+
		"\2\2\u00b2\u00b3\7.\2\2\u00b3\u00bc\7\30\2\2\u00b4\u00b9\5\n\6\2\u00b5"+
		"\u00b6\7\32\2\2\u00b6\u00b8\5\n\6\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3"+
		"\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb"+
		"\u00b9\3\2\2\2\u00bc\u00b4\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2"+
		"\2\2\u00be\u00c0\7\31\2\2\u00bf\u0097\3\2\2\2\u00bf\u009a\3\2\2\2\u00bf"+
		"\u009d\3\2\2\2\u00bf\u00a0\3\2\2\2\u00bf\u00a3\3\2\2\2\u00bf\u00a6\3\2"+
		"\2\2\u00bf\u00a9\3\2\2\2\u00bf\u00ac\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1"+
		"\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\13\3\2\2\2\u00c3\u00c1\3\2\2"+
		"\2\25\21\27\37+.<>ORis{\177\u0095\u00af\u00b9\u00bc\u00bf\u00c1";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}