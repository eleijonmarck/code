defmodule MiscTest do
  use ExUnit.Case

  test "multiply will multiply two numbers" do
    assert Misc.multiply(3,4) == 12
  end
end
