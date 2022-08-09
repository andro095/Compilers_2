// Generated from YAPL/Yapl.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link YaplParser}.
 */
public interface YaplListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link YaplParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(YaplParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link YaplParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(YaplParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link YaplParser#class}.
	 * @param ctx the parse tree
	 */
	void enterClass(YaplParser.ClassContext ctx);
	/**
	 * Exit a parse tree produced by {@link YaplParser#class}.
	 * @param ctx the parse tree
	 */
	void exitClass(YaplParser.ClassContext ctx);
	/**
	 * Enter a parse tree produced by {@link YaplParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterFeature(YaplParser.FeatureContext ctx);
	/**
	 * Exit a parse tree produced by {@link YaplParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitFeature(YaplParser.FeatureContext ctx);
	/**
	 * Enter a parse tree produced by {@link YaplParser#formal}.
	 * @param ctx the parse tree
	 */
	void enterFormal(YaplParser.FormalContext ctx);
	/**
	 * Exit a parse tree produced by {@link YaplParser#formal}.
	 * @param ctx the parse tree
	 */
	void exitFormal(YaplParser.FormalContext ctx);
	/**
	 * Enter a parse tree produced by {@link YaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(YaplParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link YaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(YaplParser.ExprContext ctx);
}